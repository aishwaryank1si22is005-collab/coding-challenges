from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = "healwell_secret_key"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

all_services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

all_costs = [
    500,
    300,
    800,
    1500,
    4000,
    7000
]

services_of_day = []
patient_details = {}
selected_services = []
selected_costs = []


@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        if request.form["username"] == ADMIN_USERNAME and request.form["password"] == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("add_services"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/add-services", methods=["GET", "POST"])
def add_services():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    error = ""

    if request.method == "POST":
        selected_service = request.form["service_name"]
        if selected_service in services_of_day:
            error = "Service already added!"
        else:
            services_of_day.append(selected_service)

    return render_template(
        "admin_services.html",
        all_services=all_services,
        services=services_of_day,
        all_costs=all_costs,
        error=error
    )


@app.route("/patient", methods=["GET", "POST"])
def patient():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    error = ""

    if request.method == "POST":
        contact = request.form["contact"]

        # Phone number validation
        if not re.fullmatch(r"[6-9][0-9]{9}", contact):
            error = "Please Enter the valid number"
            return render_template("patient_form.html", error=error)

        patient_details["name"] = request.form["name"]
        patient_details["age"] = int(request.form["age"])
        patient_details["gender"] = request.form["gender"]
        patient_details["contact"] = contact

        return redirect(url_for("select_services"))

    return render_template("patient_form.html", error=error)


@app.route("/select-services", methods=["GET", "POST"])
def select_services():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    selected_services.clear()
    selected_costs.clear()

    if request.method == "POST":
        chosen_services = request.form.getlist("services")

        for service in chosen_services:
            selected_services.append(service)
            cost = all_costs[all_services.index(service)]
            selected_costs.append(cost)

        return redirect(url_for("invoice"))

    return render_template("select_services.html", services=services_of_day)


@app.route("/invoice")
def invoice():
    subtotal = sum(selected_costs)

    discount = 0
    if patient_details.get("age", 0) >= 60:
        discount += subtotal * 0.10
    if subtotal > 5000:
        discount += subtotal * 0.05

    total_after_discount = subtotal - discount
    gst = total_after_discount * 0.18
    grand_total = total_after_discount + gst

    return render_template(
        "invoice.html",
        patient=patient_details,
        services=selected_services,
        costs=selected_costs,
        subtotal=subtotal,
        discount=discount,
        gst=gst,
        grand_total=grand_total
    )


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

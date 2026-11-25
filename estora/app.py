
from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template('index.html')


# About Page
@app.route("/about")
def about():
    return render_template('about.html')


# Explore Properties
@app.route("/properties")
def properties():
    return render_template('properties.html')


# Property Details
@app.route("/property-details")
def property_details():
    return render_template('property_details.html')


# Services Page
@app.route("/services")
def services():
    return render_template('services.html')


# Dealer Profile
@app.route("/dealer-profile")
def dealer_profile():
    return render_template('dealer_profile.html')


# Dealer Dashboard
@app.route("/dealer-dashboard")
def dealer_dashboard():
    return render_template('dealer_dashboard.html')


# Saved Properties
@app.route("/saved-properties")
def saved_properties():
    return render_template('saved_properties.html')


# Contact Page
@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)

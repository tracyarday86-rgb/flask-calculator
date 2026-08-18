from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
  result = None
  error = None

  if request.method == "POST":
    num1_str = request.form.get("num1")
    num2_str = request.form.get("num2")
    operation = request.form.get("operation")

    # Check for empty input fields
    if not num1_str or not num2_str:
      error = "Please enter both numbers."
    else:
      try:
        num1 = float(num1_str)
        num2 = float(num2_str)

        if operation == "add":
          calc_result = num1 + num2
        elif operation == "subtract":
          calc_result = num1 - num2
        elif operation == "multiply":
          calc_result = num1 * num2
        elif operation == "divide":
          if num2 == 0:
            error = "Division by zero is not allowed."
            calc_result = None
          else:
            calc_result = num1 / num2
        else:
          error = "Invalid operation selected."
          calc_result = None

        # If we have a result, check if it's a whole number (e.g., 100.0 -> 100)
        if calc_result is not None:
          if calc_result.is_integer():
            result = int(calc_result)
          else:
            result = calc_result

      except ValueError:
        error = "The numbers must be valid numeric values."

  return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
  app.run(debug=True)

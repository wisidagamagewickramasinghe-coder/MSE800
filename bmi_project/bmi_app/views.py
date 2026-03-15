from django.shortcuts import render
from .gemini_service import generate_ai_plan


def bmi_calculator(request):
    bmi = None
    category = None
    ai_plan = None
    error = None

    height = ""
    weight = ""
    age = ""
    gender = ""

    if request.method == "POST":
        height = request.POST.get("height", "").strip()
        weight = request.POST.get("weight", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()

        try:
            height_cm = float(height)
            weight_kg = float(weight)
            age_value = int(age)

            if height_cm <= 0 or weight_kg <= 0 or age_value <= 0:
                error = "Height, weight, and age must be positive values."
            elif gender.lower() not in ["male", "female"]:
                error = "Please select a valid gender."
            else:
                height_m = height_cm / 100
                bmi = round(weight_kg / (height_m ** 2), 2)

                if bmi < 20:
                    category = "Underweight"
                elif bmi < 25:
                    category = "Normal"
                else:
                    category = "Overweight"

                ai_plan = generate_ai_plan(bmi, age_value, gender, category)
                error = None

        except ValueError:
            error = "Please enter valid numeric values."
        except Exception as e:
            error = f"Gemini API error: {str(e)}"

    return render(request, "bmi.html", {
        "bmi": bmi,
        "category": category,
        "ai_plan": ai_plan,
        "error": error,
        "height": height,
        "weight": weight,
        "age": age,
        "gender": gender,
    })
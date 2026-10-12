from django.shortcuts import render, redirect

def student_form(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        student_id = request.POST.get("student_id")

        # Validation
        if not name or not student_id:
            return render(request, "form.html", {
                "error": "Student Name and Student ID are required."
            })

        # Collect all values
        major = request.POST.get("major")
        standing = request.POST.get("standing")
        languages = request.POST.getlist("languages")
        grad_year = request.POST.get("grad_year")
        comments = request.POST.get("comments")

        # Pass data to results page
        context = {
            "name": name,
            "student_id": student_id,
            "major": major,
            "standing": standing,
            "languages": languages,
            "grad_year": grad_year,
            "comments": comments,
        }

        return render(request, "results.html", context)

    return render(request, "form.html")

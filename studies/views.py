from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm
from django.contrib import messages
import logging
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)
def homepage(request):
    try:
        return render(request, 'studies/homepage.html')
    except Exception as e:
        return HttpResponse("An error occurred while loading the homepage.", status=500)

def study_list(request):
    try:
        studies = Study.objects.all() 
        return render(request, 'studies/study_list.html', {'studies': studies})
    except Exception as e:
        return HttpResponse("An unexpected error occurred while loading studies.", status=500)

def main_view(request):
    try:
        studies = Study.objects.all()
        logger.info(f"Retrieved {studies.count()} studies.")  # Log the count of studies
    except Exception as e:
        logger.error(f"An error occurred while fetching studies: {e}")
        return HttpResponse("An error occurred while loading the studies. Please try again later.", status=500)

    return render(request, 'studies/main_view.html', {'studies': studies})


def add_study(request):
    try:
        if request.method == 'POST':
            form = StudyForm(request.POST)
            if form.is_valid():
                form.save()
                logger.info("New study added successfully.")
                return redirect('main_view')  
            else:
                logger.warning("Form validation failed while adding study.")
                return render(request, 'studies/add_study.html', {'form': form})
        else:
            form = StudyForm()
            return render(request, 'studies/add_study.html', {'form': form})
    except Exception as e:
        logger.error(f"An error occurred while adding the study: {e}")
        return HttpResponse("An error occurred while adding the study.", status=500)

def view_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        return render(request, 'studies/view_study.html', {'study': study})
    except Exception as e:
        logger.error("Error viewing study: %s", e)
        return HttpResponse("An error occurred while viewing the study.", status=500)
    
def edit_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        if request.method == 'POST':
            form = StudyForm(request.POST, instance=study)
            if form.is_valid():
                form.save()
                return redirect('main_view')
        else:
            form = StudyForm(instance=study)
        return render(request, 'studies/edit_study.html', {'form': form, 'study': study})
    except Exception as e:
        logger.error("Error editing study: %s", e)
        return HttpResponse("An error occurred while editing the study.", status=500)


# def delete_study(request, study_id):
#     try:
#         study = get_object_or_404(Study, id=study_id)
#         study.delete()
#         messages.success(request, "Study deleted successfully.")
#     except Exception as e:
#         # Log the error for debugging (optional)
#         print(f"Error deleting study with id {study_id}: {e}")
#         messages.error(request, "An error occurred while deleting the study.")
#     return redirect('main_view')

def delete_selected_studies(request):
    if request.method == "POST":
        selected_ids = request.POST.getlist('studies_to_delete')
        print(selected_ids)

        Study.objects.filter(id__in=selected_ids).delete()
        print(Study.objects.filter(id__in=selected_ids))
        messages.success(request, "Selected studies have been deleted.")
    return redirect('main_view')



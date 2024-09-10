from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from student.models.student import Student
from teacher.models.teacher import Teacher
from user.models.user import User
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import openpyxl

@login_required(login_url='/')
def index(request):
    return render(request, 'rapport/index.html')

@login_required(login_url='/')
def generate_report(request):
    if request.method == 'POST':
        data_type = request.POST.get('data_type', "")  # Type de données (student, teacher, user)
        button = request.POST.get('button', "")        # Type de fichier (pdf, excel)

        # Récupération des données et définition du préfixe de nom de fichier
        if data_type == 'student':
            data = Student.objects.all()
            filename_prefix = "élèves"
        elif data_type == 'teacher':
            data = Teacher.objects.all()
            filename_prefix = "professeurs"
        elif data_type == 'user':
            data = User.objects.all()
            filename_prefix = "utilisateurs"
        else:
            return HttpResponse("Type de données non valide", status=400)

        # Génération du fichier en fonction du format demandé
        if button == 'pdf':
            return generate_pdf(data, filename_prefix)
        elif button == 'excel':
            return generate_excel(data, filename_prefix)
        else:
            return HttpResponse("Type de fichier non valide", status=400)

def generate_pdf(data, filename_prefix):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename_prefix}.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    elements = []

    # Title
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph(f"Liste des {filename_prefix}", title_style)
    elements.append(title)
    
    # Define column headers
    if filename_prefix == "élèves":
        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Numéro de téléphone", "URL", "Genre", "Matricule", "Numéro du père", ]
    elif filename_prefix == "professeurs":
        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Numéro de téléphone", "URL", "Genre", "Disponible", "Spécialité", ]
    elif filename_prefix == "utilisateurs":
        headers = ["ID", "Nom d'utilisateur", "Nom", "Prénom", "nom d'utilisateur"]

    # Prepare data rows
    data_rows = []
    for obj in data:
        row = [
            obj.id,
            obj.first_name,
            obj.last_name
        ]
        if filename_prefix == "élèves":
            row += [ obj.birthday, obj.phone_number, obj.url_picture, obj.gender, obj.matricule, obj.phone_number_father]
        elif filename_prefix == "professeurs":
            row += [obj.birthday, obj.phone_number, obj.url_picture, obj.gender, obj.available, obj.speciality,]
        elif filename_prefix == "utilisateurs":
            row += [obj.username, ]
        data_rows.append(row)

    # Create table
    table_data = [headers] + data_rows
    table = Table(table_data)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#d0d0d0'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BACKGROUND', (0, 1), (-1, -1), '#f9f9f9'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ])
    table.setStyle(style)
    elements.append(table)

    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    response.write(buffer.read())
    return response

def generate_excel(data, filename_prefix):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename_prefix}.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"Liste des {filename_prefix}"

    # Ajouter les en-têtes en fonction du type de données
    if filename_prefix == "élèves":
        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Numéro de téléphone", "URL", "Genre", "Matricule", "Numéro du père", ]
    elif filename_prefix == "professeurs":
        headers = ["ID", "Nom", "Prénom", "Date de naissance", "Numéro de téléphone", "URL", "Genre", "Disponible", "Spécialité", ]
    elif filename_prefix == "utilisateurs":
        headers = ["ID", "Nom d'utilisateur", "Nom", "Prénom"]
    else:
        return HttpResponse("Type de données non valide", status=400)

    ws.append(headers)

    # Ajouter les données dans les colonnes
    for obj in data:
        if filename_prefix == "élèves":
            row = [obj.id, obj.first_name, obj.last_name, obj.birthday, obj.phone_number, obj.url_picture, obj.gender, obj.matricule, obj.phone_number_father]
        elif filename_prefix == "professeurs":
            row = [obj.id, obj.first_name, obj.last_name, obj.birthday, obj.phone_number, obj.url_picture, obj.gender, obj.available, obj.speciality, ]
        elif filename_prefix == "utilisateurs":
            row = [obj.id, obj.username, obj.first_name, obj.last_name]
        ws.append(row)

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    response.write(buffer.read())
    return response

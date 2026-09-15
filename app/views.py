from rest_framework.views import APIView as ApiView, Response
from app.models import Projects
from app.serializers import ProjectSerializer
from rest_framework import status

class ProjectView(ApiView):
    
    def get (self, request, id=None):
        if id is not None:
            try:
                project = Projects.objects.get(id=id)
            except Projects.DoesNotExist:
                return Response(
                    {"error": "Proyecto no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                ) 
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        try:
            project = Projects.objects.get(id=id)
        except Projects.DoesNotExist:
            return Response (
                {"error": "Proyecto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer =ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            project = Projects.objects.get(id=id)
        except Projects.DoesNotExist:
            return Response(
                {"error": "Proyecto no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        project.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
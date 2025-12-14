from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, MovieSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "user": user.username,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED
        )


class MovieListCreateView(ListCreateAPIView):
    
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Movie.objects.filter(user=self.request.user)
        watched_param = self.request.query_params.get('watched')
        if watched_param is not None:
            if watched_param.lower() == 'true':
                queryset = queryset.filter(watched=True)
            elif watched_param.lower() == 'false':
                queryset = queryset.filter(watched=False)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
class MovieDeleteView(DestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)
    
    
class MovieToggleWatchedView(UpdateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        # toggle the watched status
        obj.watched = not obj.watched
        obj.save()
        return obj
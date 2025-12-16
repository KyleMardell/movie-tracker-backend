from rest_framework import permissions, status, filters
from rest_framework.generics import CreateAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, MovieSerializer


"""
Register user view
Allows new users to create an account, 
adding the user credentials to the database.
Returns JWT tokens for auto log in upon sign up.
"""
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


"""
Movie list create view
Lets users add new movies to their movies list
Returns a list of the users saved movies
Allows filtering by watched status and search by movie title
"""
class MovieListCreateView(ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['created_on', 'title']
    ordering = ['-created_on']
    search_fields = ['title']

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
    

"""
Delete movie view
Lets users delete movies from their list
User must be authenticated and the movie owner.
"""
class MovieDeleteView(DestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)
    

"""
Movie toggle watched view
Lets users toggle a movies watched status
user must be authenticated and the movie owner
"""
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
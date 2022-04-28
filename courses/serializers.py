from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag,User,Comment, Action, Rating, LessonView

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'created_date', 'category']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image','course', 'created_date', 'update_date', 'tags']


class LessonDetailSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name',
                  'username','password','email','date_joined']
        extra_kwargs = {
            'password':{'write_only':'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','created_date','updated_date']


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ['id', 'type', 'created_date']


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rate', 'created_date']


class LessonViewSerializer(ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['id', 'views', 'lesson']
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Course, Review, Enrollment, TutorEnrollment
from users.models import CustomUser
from users.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    students = EnrollmentSerializer(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    tutor = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        course = Course.objects.create(tutor=self.context['request'].user,**validated_data)
        if course:
            return course
        

    def update(self, instance, validated_data):
        instance = super(CourseSerializer, self).update(instance, validated_data)
        instance.save()
        return instance
    
    


    
class TutorEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorEnrollment
        fields = '__all__'

    

from rest_framework import serializers
from .models import User, JobType, PremiumJob, Subject, Order


class UserReadSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    def get_roles(self, user):
        roles_list = []
        for group in user.groups.all():
            roles_list.append(group.name)
        return roles_list

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'is_superuser', 'roles')


class UserWriteSerializer(serializers.ModelSerializer):
    """
    Serializer Class Used to Create User
    """
    password = serializers.CharField(write_only=True)
    surname = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    role = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            surname=validated_data['surname'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'first_name', 'surname',
                  'password', 'role', 'phone_number')


class PremiumJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumJob
        fields = ['id', 'name', 'price']


class PremiumJobWriteSerializer(serializers.ModelSerializer):
    """
    Serializer Class Used to Create User
    """
    name = serializers.CharField(write_only=True)
    price = serializers.FloatField()

    def create(self, validated_data):
        print(validated_data)
        premium_job = PremiumJob.objects.create(
            name=validated_data['name'],
            price=validated_data['price']
        )
        premium_job.save()
        return premium_job

    class Meta:
        model = PremiumJob
        fields = ('id', 'name', 'price')


class OrderWriteSerializer(serializers.ModelSerializer):
    """
    Serializer Class used to write order
    """
    subject = serializers.PrimaryKeyRelatedField(
        allow_null=False, queryset=Subject.objects.all())
    job_type = serializers.PrimaryKeyRelatedField(
        allow_null=False, queryset=JobType.objects.all())
    premium_job = serializers.PrimaryKeyRelatedField(
        allow_null=False, queryset=PremiumJob.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(
        allow_null=False, queryset=User.objects.all())
    word_count = serializers.IntegerField()
    company = serializers.CharField(write_only=True)
    company_url = serializers.CharField(write_only=True)
    keywords = serializers.CharField(write_only=True)
    deadline = serializers.DateTimeField()
    brief = serializers.CharField(write_only=True)

    def create(self, validated_data):
        print(validated_data)
        order = Order.objects.create(**validated_data)
        order.save()
        return order

    class Meta:
        model = Order
        fields = ('id', 'subject', 'word_count', 'company',
                  'company_url', 'keywords', 'deadline', 'brief', 'created_by', 'job_type', 'premium_job')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'subject', 'word_count', 'company',
                  'company_url', 'keywords', 'deadline', 'brief']

from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from drf_rw_serializers.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Quiz, Question
from django.shortcuts import get_object_or_404


class ExceptionDetailSerializer(serializers.Serializer):
    status_code = serializers.IntegerField(read_only=True)
    detail = serializers.CharField(read_only=True)


class QuizGetWriteSerializer(serializers.Serializer):
    pk = serializers.IntegerField()


class AnswerReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    false_answer_1 = serializers.CharField(read_only=True)
    false_answer_2 = serializers.CharField(read_only=True)
    false_answer_3 = serializers.CharField(read_only=True)
    true_answer = serializers.CharField(read_only=True)


class QuestionReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_number = serializers.IntegerField(read_only=True)
    question = serializers.CharField(read_only=True)
    answer = AnswerReadSerializer(read_only=True)


class QuizGetReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    question = QuestionReadSerializer(read_only=True, many=True)


@extend_schema(tags=["Quiz list"])
class QuizListApi(GenericAPIView):

    read_serializer_class = QuizGetReadSerializer

    @extend_schema(
        summary='Получить список викторин',
        responses={
            status.HTTP_200_OK: QuizGetReadSerializer,
        })
    def get(self, *args, **kwargs):
        self.queryset = get_quiz_queryset_from_db()
        page = self.paginator.paginate_queryset(self.queryset, self.request)
        read_serializer = self.get_read_serializer(page, many=True)
        return self.paginator.get_paginated_response(data=read_serializer.data)


quiz_list_api = QuizListApi.as_view()


@extend_schema(tags=["Quiz detail"])
class QuizDetailApi(GenericAPIView):

    write_serializer_class = QuizGetWriteSerializer
    read_serializer_class = QuizGetReadSerializer

    @extend_schema(
        summary='Получить детальную информацию о викторине',
        responses={
            status.HTTP_200_OK: QuizGetReadSerializer,
            status.HTTP_404_NOT_FOUND: ExceptionDetailSerializer
        })
    def get(self, *args, **kwargs):
        write_serializer = self.get_write_serializer(data=self.kwargs)
        write_serializer.is_valid(raise_exception=True)
        self.queryset = get_quiz_queryset_from_db()
        quiz_object = get_object_or_404(self.queryset, **write_serializer.validated_data)
        read_serializer = self.get_read_serializer(quiz_object)
        return Response(data=read_serializer.data, status=status.HTTP_200_OK)


quiz_detail_api = QuizDetailApi.as_view()


def get_quiz_queryset_from_db():
    quiz = (
            Quiz.objects.prefetch_related(
                Prefetch(
                    lookup='questions', queryset=Question.objects.prefetch_related(
                        Prefetch(
                            lookup='answers', to_attr='answer'
                        )
                    ), to_attr='question'
                )
            )
        )
    return quiz


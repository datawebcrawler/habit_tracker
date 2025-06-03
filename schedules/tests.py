# schedules/tests.py
import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser # Assumindo que CustomUser está em accounts.models
from activities.models import Activity
from .models import Schedule

class ScheduleCRUDTests(TestCase):

    def setUp(self):
        # Criar um usuário de teste
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            name='Test User'
        )
        self.client.login(email='test@example.com', password='password123')

        # Criar uma atividade de teste associada ao usuário
        self.activity = Activity.objects.create(
            user=self.user,
            activity="Test Activity",
            category="Testing",
            frequency="unica"
        )

        # Criar um agendamento de teste
        self.schedule = Schedule.objects.create(
            activity=self.activity,
            scheduled_date=datetime.date.today() + datetime.timedelta(days=1),
            start_time=datetime.time(10, 0, 0),
            status='pendente'
        )

    def test_schedule_list_view(self):
        """Testa se a lista de agendamentos é exibida corretamente."""
        response = self.client.get(reverse('schedules:schedule_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.activity.activity)
        self.assertTemplateUsed(response, 'schedules/list.html')

    def test_schedule_create_view_get(self):
        """Testa o GET da view de criação de agendamento."""
        response = self.client.get(reverse('schedules:schedule_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'schedules/form.html')

    def test_schedule_create_view_post(self):
        """Testa o POST da view de criação de agendamento."""
        new_activity = Activity.objects.create(
            user=self.user,
            activity="Another Activity for schedule",
            category="Testing",
            frequency="diaria"
        )
        data = {
            'activity': new_activity.id,
            'scheduled_date': datetime.date.today() + datetime.timedelta(days=2),
            'start_time': '14:00',
            'status': 'pendente'
        }
        response = self.client.post(reverse('schedules:schedule_create'), data)
        self.assertEqual(response.status_code, 302) # Redirecionamento após sucesso
        self.assertTrue(Schedule.objects.filter(activity=new_activity, status='pendente').exists())

    def test_schedule_update_view_get(self):
        """Testa o GET da view de atualização de agendamento."""
        response = self.client.get(reverse('schedules:schedule_update', args=[self.schedule.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.activity.activity)
        self.assertTemplateUsed(response, 'schedules/form.html')

    def test_schedule_update_view_post(self):
        """Testa o POST da view de atualização de agendamento."""
        updated_date = datetime.date.today() + datetime.timedelta(days=5)
        data = {
            'activity': self.activity.id,
            'scheduled_date': updated_date,
            'start_time': self.schedule.start_time.strftime('%H:%M'),
            'status': 'adiado'
        }
        response = self.client.post(reverse('schedules:schedule_update', args=[self.schedule.id]), data)
        self.assertEqual(response.status_code, 302) # Redirecionamento após sucesso
        self.schedule.refresh_from_db()
        self.assertEqual(self.schedule.scheduled_date, updated_date)
        self.assertEqual(self.schedule.status, 'adiado')

    def test_schedule_delete_view(self):
        """Testa a exclusão de um agendamento."""
        schedule_to_delete = Schedule.objects.create(
            activity=self.activity,
            scheduled_date=datetime.date.today() + datetime.timedelta(days=3),
            start_time=datetime.time(11, 0, 0),
            status='pendente'
        )
        response = self.client.post(reverse('schedules:schedule_delete', args=[schedule_to_delete.id]))
        self.assertEqual(response.status_code, 302) # Redirecionamento após sucesso
        self.assertFalse(Schedule.objects.filter(id=schedule_to_delete.id).exists())

    def test_schedule_check_in_view(self):
        """Testa a funcionalidade de check-in de um agendamento."""
        schedule_to_checkin = Schedule.objects.create(
            activity=self.activity,
            scheduled_date=datetime.date.today(),
            start_time=datetime.time(12, 0, 0),
            status='pendente'
        )
        response = self.client.get(reverse('schedules:schedule_check_in', args=[schedule_to_checkin.id]))
        self.assertEqual(response.status_code, 302) # Redirecionamento após sucesso
        schedule_to_checkin.refresh_from_db()
        self.assertEqual(schedule_to_checkin.status, 'feito')

    def test_schedule_form_filters_activities_by_user(self):
        """Testa se o formulário de agendamento filtra atividades para o usuário logado."""
        # Criar um segundo usuário e uma atividade para ele
        other_user = CustomUser.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='password123',
            name='Other User'
        )
        Activity.objects.create(
            user=other_user,
            activity="Other User Activity",
        )

        response = self.client.get(reverse('schedules:schedule_create'))
        self.assertEqual(response.status_code, 200)
        # Verifica se a atividade do usuário logado está no formulário
        self.assertContains(response, self.activity.activity)
        # Verifica se a atividade do outro usuário NÃO está no formulário
        self.assertNotContains(response, "Other User Activity")

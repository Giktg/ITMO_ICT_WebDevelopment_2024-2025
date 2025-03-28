# Описание моделей

## Floor

Представляет этажи в здании

#### Поля:

- **floor** - первичный ключ, номер этажа

## Apartments

Описывает апартаменты в здании

#### Поля:

- **apartment_number** - первичный ключ, номер апартамента
- **rooms** - количество комнат в апартаментах
- **price** - цена за проживание
- **floor** - внешний ключ, связывающий номер с этажом
- **status** - статус номера (свободен, сдан, забронирован, на ремонте)
- **phone** - телефон в номере

## Guest

Содержит информацию об уборщиках

#### Поля:

- **passport_number** - первичный ключ, номер паспорта гостя
- **guest_name** - имя гостя
- **city** - город, из которого гость прибыл


## Resident

Описывает информацию о проживающих в апартаментах

#### Поля:

- **passport_number** - внешний ключ, гость, живущий в номере
- **apartment_number** - внешний ключ, номер апартаментов
- **check_in** - дата заселения
- **check_out** - дата выселения


## Cleaner

Содержит информацию об уборщиках

#### Поля:

- **cleaner_name** - первичный ключ, имя уборщика



## CleanSchedule

Содержит информацию о расписании уборки для каждого уборщика и этажа.

#### Поля:

- **cleaner_id** - внешний ключ, кто убирает
- **floor** - внешний ключ, какой этаж убирает
- **day** - день недели


#Сериалайзеры

___
<br/>


## Auth сериализаторы

### RegistrationSerializer <br>

**Описание:** Позволяет регистрировать новых пользователей <br>

**Поля:** <br>
- `username`: имя пользователя <br>
- `password`: пароль пользователя <br>
- `password2`: подтверждение пароля <br>

**Методы:** <br>
- `validate`: проверяет соответствие пароля и его подтверждения <br>
- `create`: создает нового пользователя <br>

---

### LoginSerializer <br>

**Описание:** Сериализатор для аутентификации пользователей <br>

**Поля:** <br>
- `username`: имя пользователя <br>
- `password`: пароль пользователя <br>

---

### LogoutSerializer <br>

**Описание:** Сериализатор для выхода пользователя из системы <br>

**Поля:** отсутствуют <br>

---

### PasswordChangeSerializer <br>

**Описание:** Позволяет изменить пароль пользователя <br>

**Поля:** <br>
- `current_password`: текущий пароль пользователя <br>
- `new_password`: новый пароль пользователя <br>

**Методы:** <br>
- `validate_current_password`: проверяет текущий пароль пользователя перед изменением <br>

---

## Основные сериализаторы


### ApartmentsSerializer <br>

**Описание:** Сериализатор для модели Apartments <br>

**Поля:** все поля модели <br>

---

### GuestSerializer <br>

**Описание:** Сериализатор для модели Guest <br>

**Поля:** все поля модели <br>

---

### FloorSerializer <br>

**Описание:** Сериализатор для модели Floor <br>

**Поля:** все поля модели <br>

---

### ResidentSerializer <br>

**Описание:** Сериализатор для модели Resident <br>

**Поля:** все поля модели <br>

---

### CleanerSerializer <br>

**Описание:** Сериализатор для модели Cleaner <br>

**Поля:** все поля модели <br>

---

### CleanScheduleSerializer <br>

**Описание:** Сериализатор для модели CleanSchedule <br>

**Поля:** все поля модели <br>

---

## Дополнительные сериализаторы

### FindGuestSerializer <br>

**Описание:** Сериализатор для поиска гостей по городу <br>

**Поля:** <br>
- `city`: город <br>

---

### FindResidentSerializer <br>

**Описание:** Сериализатор для поиска жильцов без номера паспорта <br>

**Поля:** все поля модели, кроме номера паспорта <br>

---

### ShowResidentSerializer <br>

**Описание:** Сериализатор для отображения информации о жильце <br>

**Поля:** все поля модели <br>

---

### FindScheduleSerializer <br>

**Описание:** Сериализатор для поиска расписания уборки <br>

**Поля:** <br>
- `day`: день недели <br>
- `resident`: имя жильца <br>

---

### OtherResidentsSerializer <br>

**Описание:** Сериализатор для отображения других жильцов <br>

**Поля:** <br>
- `passport_number`: номер паспорта <br>
- `apartment_number`: номер апартамента <br>
- `check_in`: дата заезда <br>
- `check_out`: дата выезда <br>

---

### CleanerForResident <br>

**Описание:** Сериализатор для назначения уборщика жильцу <br>

**Поля:** <br>
- `guest_name`: имя гостя <br>
- `day`: день недели <br>

---

### ShowCleanerSerializer <br>

**Описание:** Сериализатор для отображения имени уборщика <br>

**Поля:** <br>
- `cleaner_name`: имя уборщика <br>

---

### ReportSerializer <br>

**Описание:** Сериализатор для создания квартального отчета <br>

**Поля:** <br>
- `apartment_number`: номер апартамента <br>

**Методы:** <br>
- `get_total_clients`: возвращает количество клиентов за указанный период <br>
- `get_total_income`: возвращает общий доход за указанный период <br>






# Роутер
___
<br/>

## hotel/urls.ry
<br/>

```python
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('hotel.urls')),
]
```

<br/>

## lab3/urls.ry
<br/>

```python
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.SimpleRouter()

router.register('apartments', viewset=views.ApartmentsViewSet)
router.register('guest', viewset=views.GuestViewSet)
router.register('floor', viewset=views.FloorViewSet)
router.register('resident', viewset=views.ResidentViewSet)
router.register('cleaner', viewset=views.CleanerViewSet)
router.register('schedule', viewset=views.CleanScheduleViewSet)
router.register('report', viewset=views.ReportViewSet, basename='quarterly_report')



urlpatterns = [
    path('report/<str:quarter>/', views.ReportViewSet.as_view({'get': 'list'}), name='report'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', views.ChangePasswordView.as_view(), name='change-password'),
    path('', include(router.urls)),
]

```
<br/>

# Эндпоинты
___
<br/>

## Регистрация

- **Эндпоинт:** /register/
- **Метод:** POST
- **Описание:** Регистрация нового пользователя <br>

## Вход

- **Эндпоинт:** /login/
- **Метод:** POST
- **Описание:** Вход пользователя в систему <br>

## Выход

- **Эндпоинт:** /logout/
- **Метод:** POST
- **Описание:** Выход пользователя из системы <br>

## Изменение пароля

- **Эндпоинт:** /change-password/{user_id}/
- **Метод:** POST
- **Описание:** Изменение пароля пользователя с идентификатором {user_id} <br>

## Список апартаментов

- **Эндпоинт:** /apartments/
- **Метод:** GET
- **Описание:** Получение списка всех апартаментов <br>

## Список гостей

- **Эндпоинт:** /guest/
- **Метод:** GET
- **Описание:** Получение списка всех гостей <br>

## Список этажей

- **Эндпоинт:** /floor/
- **Метод:** GET
- **Описание:** Получение списка всех этажей <br>

## Список жильцов

- **Эндпоинт:** /resident/
- **Метод:** GET
- **Описание:** Получение списка всех жильцов <br>

## Список уборщиков

- **Эндпоинт:** /cleaner/
- **Метод:** GET
- **Описание:** Получение списка всех уборщиков <br>

## Расписание уборки

- **Эндпоинт:** /schedule/
- **Метод:** GET
- **Описание:** Получение списка всех расписаний уборки <br>

## Отчет

- **Эндпоинт:** /report/{quarter}/
- **Метод:** GET
- **Описание:** Получение квартального отчета за указанный квартал <br>































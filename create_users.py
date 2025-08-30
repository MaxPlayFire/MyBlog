import django_setup
from blog import models

# --- Subjects ---
s1 = models.Subject(name="Math")
s2 = models.Subject(name="History")
s1.save()
s2.save()

# --- Teachers ---
t1 = models.Teacher(name="Ivan", surname="Petrenko", subject=s1, email="ivan@example.com", age=35)
t2 = models.Teacher(name="Olena", surname="Shevchenko", subject=s2, email="olena@example.com", age=40)
t1.save()
t2.save()

c1 = models.Class(name="Class A", teacher=t1, number=1)
c2 = models.Class(name="Class B", teacher=t2, number=2)
c3 = models.Class(name="Class C", teacher=t2, number=3)
c1.save()
c2.save()
c3.save()

u1 = models.Student(name="Andrii", surname="Koval", email="andrii@example.com", age=12, student_class=c1)
u2 = models.Student(name="Maria", surname="Tkachenko", email="maria@example.com", age=13, student_class=c2)
u3 = models.Student(name="Oleh", surname="Bondar", email="oleh@example.com", age=14, student_class=c3)
u1.save()
u2.save()
u3.save()

S1 = models.Schedule(
    school_class=c1,
    subject=s1,
    teacher=t1,
    day_of_week="Monday",
    time="09:00:00"
)
S1.save()

print("✅ Test data created successfully!")

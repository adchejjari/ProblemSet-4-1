# ProblemSet-5

### Author : Adnane Chejjari - Master 1 Miage Apprenticeship

Please find bellow the answers to the 1st exercise :

### Question 1

**SQL :**

```
CREATE TABLE classrooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roomname NEXT NOT NULL,
    seats INTEGER DEFAULT 50 NOT NULL
)
```

**Django :**

```
from django.db import models

class Classroom(models.Model):
    roomname = models.CharField(max_length=255)
    seats = models.IntegerField(default=50)

    class Meta:
        db_table = 'classrooms'
        managed = True
        verbose_name = 'Classroom'
        verbose_name_plural = 'Classrooms'
```

The "Meta" class is added in order to allow us to customize certain parameters of our model.

### Question 2

**SQL :**

```
INSERT INTO classrooms (roomname, seats) VALUES ('A101', 42);
```

**Django :**

```
from myapp.models import Classroom


classroom = Classroom(roomname='A101', seats=42)
classroom.save()
```

**SQL :**

```
INSERT INTO classrooms (roomname) VALUES ('A101');
```

**Django :**

```
from myapp.models import Classroom


classroom = Classroom(roomname='A102')
classroom.save()
```

Please note that the `seats` attribute will be set to it's default value 50.

### Question 3

**SQL :**

```
SELECT * FROM classrooms WHERE seats > 45;
```

**Diango :**

```
from myapp.models import Classroom

classrooms = Classroom.objects.filter(seats__gt=45)
```

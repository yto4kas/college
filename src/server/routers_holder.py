from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from src.database.models import *

UserRouter = AuthRouter("Users", Users)
subjectRouter = Router("subject", subject)
TeachersRouter = Router("Teachers", Teachers)
StudentsRouter = Router("Students", Students)
CoursesRouter = Router("Courses", Courses)
EnrollmentRouter = Router("Enrollment", Enrollment)
GradesRouter = Router("Grades", Grades)

routers = (UserRouter.router, subjectRouter.router, TeachersRouter.router, StudentsRouter.router, CoursesRouter.router, Enrollment.router, GradesRouter.router)

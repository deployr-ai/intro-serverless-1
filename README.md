# Creá un scraper automático de Twitter en AWS en cinco sencillos pasos (Intro a Serverless Pt. 1)
Repo que acompaña el artículo "Creá un scraper automático de Twitter en AWS en cinco sencillos pasos (Intro a Serverless Pt. 1)", disponible [en este link](https://deployr.medium.com/control-de-accesos-en-aws-c%C3%B3mo-trabajo-en-la-nube-de-forma-segura-326260e173f3).

### ¿Qué necesitamos?
Lo que vamos a necesitar en esta etapa es:
- API Key developer de Twitter (la v2 de la API se consigue instantáneamente y a nuestros efectos nos alcanza).

- Acceso a AWS con los roles que nos permiten interactuar entre Lambda, S3 y Eventbridge. Para eso, [este artículo](https://deployr.medium.com/control-de-accesos-en-aws-c%C3%B3mo-trabajo-en-la-nube-de-forma-segura-326260e173f3) te puede servir.


- Acceso a un bucket en S3.

Como un opcional, acceso a una notebook de AWS Sagemaker (y los roles que se requieren, especialmente para conectar con S3).

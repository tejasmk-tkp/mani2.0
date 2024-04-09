from roboflow import Roboflow

rf = Roboflow(api_key="GJWbB1wT3XgyQGQGLJNC")
project = rf.workspace("myworkspace-pjfam").project("box-detection-daqza")
version = project.version(1)
dataset = version.download("tfrecord")

# The reason we have this model is that the story will take time to be created and this will carry the workflow while creating the story
# JOB is representing an intent to make a story.
# We will be checking for the status of the job to be completed.
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.sql import func

from db.database import Base

class StoryJob(Base):
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_job = Column(DateTime(timezone=True), nullable=True)

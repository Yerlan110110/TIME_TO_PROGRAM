from pydantic import BaseModel, Field, EmailStr
data = {
    'email': 'rtrutmailref.effe@w.u',
    'bio': 'Я пирожок',
    'age': 12
}

class UserSheams(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)
    
class UserAgeSheams(UserSheams):
    age: int = Field(ge=0,le=130)
     

print(UserAgeSheams(**data))

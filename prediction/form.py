from django.forms import Form

class PredictForm(Form):
    total_sqft = StringField(label="Area", validators=[Length(min=200,max=15000), DataRequired() ])
    location = SelectField(label="Location", validators=[DataRequired()])
    bhks = RadioField(label="BHKs", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),], validators=[DataRequired(),])
    bathrooms = RadioField(label="Bathrooms", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),], validators=[DataRequired()])
    submit = SubmitField(label="Submit")

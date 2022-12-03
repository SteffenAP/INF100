from uib_inf100_graphics import * 

#upcurve er antall "svingninger"
#minimum 3 svingninger, ellers dynamisk

def curves(canvas, upcurve, app):
    halfstep_low = + ((((1/upcurve)/2)*0.5) *app.width) #halvveis mellom to iterasjoner av løkken 0-50%
    fullstep_hi = + ((((1/upcurve))*0.5) *app.width) # halvveis mellom to iterasjoner av løkken 50-100%
    for _ in range(upcurve):
        ratio = ((_ + 1)/upcurve) # et forhold som gjør linjeplasseringene dynamisk ved å øke satsene til linjene med iterasjon/total
        canvas.create_line(app.width * (ratio * 0.5), app.height * 0.5, app.width * (ratio * 0.5), app.height * 0.75, fill = "green", width= 2)
        canvas.create_line(app.width * (ratio * 0.5), app.height * 0.75, (app.width * (ratio * 0.5)) + (halfstep_low) , app.height * 0.75, fill = "green", width = 2)
        canvas.create_line(app.width * (ratio * 0.5) + (halfstep_low), app.height * 0.75, app.width * (ratio * 0.5) + (halfstep_low), app.height * 0.25, fill = "green", width = 2)
        canvas.create_line(app.width * (ratio * 0.5) + (halfstep_low), app.height * 0.25, app.width * (ratio * 0.5) + (fullstep_hi) , app.height * 0.25, fill = "green", width = 2)
        canvas.create_line(app.width * (ratio * 0.5) + (fullstep_hi), app.height * 0.25, app.width * (ratio * 0.5) + (fullstep_hi), app.height * 0.5, fill = "green", width= 2)
    canvas.create_line(app.width * 0.5 + fullstep_hi, app.height * 0.5, app.width * 0.5 + fullstep_hi * 2, app.height * 0.5, fill = "green", width = 2)
    canvas.create_oval(app.width * 0.5 + fullstep_hi *2, app.height * 0.45, app.width * 0.5 + fullstep_hi * 3, app.height * 0.55, fill = "green")

def redraw_all(app, canvas):
        curves(canvas, 6, app)

run_app(width = 600, height = 400)
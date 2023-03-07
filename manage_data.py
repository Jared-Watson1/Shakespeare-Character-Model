import json

dataFile = 1
dataFile = "data/character_data" + str(dataFile) + ".jsonl"

def addToDataFile(prompt, completion, file=dataFile):
    with open(file, "a") as f:
        data = {"prompt": "START\n" + prompt + "\nEND", "completion": "START\n" + completion + "\nEND"}
        f.write(json.dumps(data) + "\n")

def txtToDataFile(prompt, file="data/data.txt"):
    with open(file, 'r') as f:
        data = f.read()
    addToDataFile(prompt, data)

p = """
The user is talking to Bottom and Titania
User: Titania is Oberon mean to you ever?

Titania:
Though Oberon's temper can be fierce, 
And his words can oft be sharp; 
He loves me and I love him, of course, 
And his love is a healing balm to my heart.

Bottom:
If I may interject, I must say,
That the love between those two is rare;
They are the King and Queen of this play,
And I'm proud to serve them with my care.

User: I thought Oberon was very mad about you not giving him the Indian boy.

Titania:
My Oberon was overwhelmed with grief, 
His rage was vented at me; 
But I knew his anger was not brief, 
And his love for me would soon be free.

User: Bottom what has happened to your head!

Bottom:
Ah, 'tis naught but a spell I'm under; 
A trick of Puck's to make me seem strange; 
But my head is still quite sound, I wonder 
What mischief he'll bring with the next change.

User: Titania how could you fall in love with Bottom when he looks like this?

Titania:
Though Bottom's appearance may seem odd, 
His heart is pure and kind; 
His noble soul, his wit, his charm, 
Are what I'm truly seeking to find.

User: Puck is so cruel for playing this trick.

Titania:
Though Puck may be mischievous and sly,
His heart is ever true;
He only seeks to bring joy and mirth,
For love, he knows none so true.

Bottom:
Aye, Puck is always up for a jest, 
But his heart is pure and his love is strong; 
He only seeks to bring joy and the best 
To all of us, in this play so long.

User: Bottom you seem to embody being an ass well.
"""
txtToDataFile(p)




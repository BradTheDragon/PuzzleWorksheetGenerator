from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import sys

# Create a PDF document
c = canvas.Canvas("worksheet.pdf", pagesize=letter)

def doMath(num1, num2, num3, oper):
  if oper == "+":
    return num1 + num2 + num3
  elif oper == "-":
    return num1 - num2 - num3
  else:
    print("Invalid operator")
    sys.exit()

def list_to_string(num_list):
  result = ''.join(str(num) for num in num_list)
  return result

def count_unique_numbers(lst):
  unique_numbers = set(lst)
  return len(unique_numbers)

def generate_numbers(num_unique):
    if num_unique > 9:
        return "Error: The number of unique numbers can not be greater than 9."
    unique_numbers = random.sample(range(1, 10), num_unique)
    duplicate_numbers = [random.choice(unique_numbers) for _ in range(8 - num_unique)]
    final_numbers = unique_numbers + duplicate_numbers
    random.shuffle(final_numbers)

    return final_numbers

def drawPolygon(vertices):
  for i in range(len(vertices)):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % len(vertices)]
    c.line(x1, y1, x2, y2)

def drawPuzzleShape(x, y):
  vertices = [(x, y), (x, y + 150), (x + 150, y + 150), (x + 150, y + 50),
              (x + 100, y + 50), (x + 100, y)]
  drawPolygon(vertices)

def drawPuzzle(x, y, column1, column2, row1, row2, numbers):
  drawPuzzleShape(x, y)
  c.setFont("Helvetica", 30)
  c.drawString(x + 10, y - 25, column1)
  c.drawString(x + 58, y - 25, column2)
  c.drawString(x + 155, y + 115, row1)
  c.drawString(x + 155, y + 70, row2)
  c.setFont("Helvetica", 25)
  c.drawString(x, y - 60, numbers, charSpace=5)

def createWorksheet(oper, difficulty):
  answers = [[], [], [], [], [], []]
  questions = {"Puzzle1": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}, 
               "Puzzle2": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}, 
               "Puzzle3": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}, 
               "Puzzle4": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}, 
               "Puzzle5": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}, 
               "Puzzle6": {"Column1": "", "Column2": "", "Row1": "", "Row2": "", "Numbers": ""}}
  if difficulty != "any":
    for i in range(len(answers)):
      numbers = generate_numbers(int(difficulty))
      answers[i] = numbers
      questions[f"Puzzle{i + 1}"]["Numbers"] = list_to_string(numbers)

      questions["Puzzle" + str(i + 1)]["Column1"] = str(doMath(answers[i][0], answers[i][3], answers[i][6], oper))
      questions["Puzzle" + str(i + 1)]["Column2"] = str(doMath(answers[i][1], answers[i][4], answers[i][7], oper))
      questions["Puzzle" + str(i + 1)]["Row1"] = str(doMath(answers[i][0], answers[i][1], answers[i][2], oper))
      questions["Puzzle" + str(i + 1)]["Row2"] = str(doMath(answers[i][3], answers[i][4], answers[i][5], oper))

      sortedList = [char for char in questions["Puzzle" + str(i + 1)]["Numbers"]]
      sortedList.sort()
      questions["Puzzle" + str(i + 1)]["Numbers"] = "".join(sortedList)
  else:
    for i in range(len(answers)):
      for x in range(8):
        answer = random.randint(1, 9)
        answers[i].append(answer)
        questions["Puzzle" + str(i + 1)]["Numbers"] = questions["Puzzle" + str(i + 1)]["Numbers"] + str(answer)

    
      questions["Puzzle" + str(i + 1)]["Column1"] = str(doMath(answers[i][0], answers[i][3], answers[i][6], oper))
      questions["Puzzle" + str(i + 1)]["Column2"] = str(doMath(answers[i][1], answers[i][4], answers[i][7], oper))
      questions["Puzzle" + str(i + 1)]["Row1"] = str(doMath(answers[i][0], answers[i][1], answers[i][2], oper))
      questions["Puzzle" + str(i + 1)]["Row2"] = str(doMath(answers[i][3], answers[i][4], answers[i][5], oper))
  
      sortedList = [char for char in questions["Puzzle" + str(i + 1)]["Numbers"]]
      sortedList.sort()
      questions["Puzzle" + str(i + 1)]["Numbers"] = "".join(sortedList)
  
  drawPuzzle(100, 600, questions["Puzzle1"]["Column1"], questions["Puzzle1"]["Column2"], questions["Puzzle1"]["Row1"], questions["Puzzle1"]["Row2"], questions["Puzzle1"]["Numbers"])
  drawPuzzle(350, 600, questions["Puzzle2"]["Column1"], questions["Puzzle2"]["Column2"], questions["Puzzle2"]["Row1"], questions["Puzzle2"]["Row2"], questions["Puzzle2"]["Numbers"])
  drawPuzzle(100, 350, questions["Puzzle3"]["Column1"], questions["Puzzle3"]["Column2"], questions["Puzzle3"]["Row1"], questions["Puzzle3"]["Row2"], questions["Puzzle3"]["Numbers"])
  drawPuzzle(350, 350, questions["Puzzle4"]["Column1"], questions["Puzzle4"]["Column2"], questions["Puzzle4"]["Row1"], questions["Puzzle4"]["Row2"], questions["Puzzle4"]["Numbers"])
  drawPuzzle(100, 100, questions["Puzzle5"]["Column1"], questions["Puzzle5"]["Column2"], questions["Puzzle5"]["Row1"], questions["Puzzle5"]["Row2"], questions["Puzzle5"]["Numbers"])
  drawPuzzle(350, 100, questions["Puzzle6"]["Column1"], questions["Puzzle6"]["Column2"], questions["Puzzle6"]["Row1"], questions["Puzzle6"]["Row2"], questions["Puzzle6"]["Numbers"])
  
  print(answers[0])
  print(answers[1])
  print(answers[2])
  print(answers[3])
  print(answers[4])
  print(answers[5])

operation = input("What operation should the puzzles be based on? (+, -): ")
difficulty = input("What difficulty should the puzzles be based on? (2-8 or any): ")
numberOfPages = int(input("How many pages?: "))
for z in range(numberOfPages):
  createWorksheet(operation, difficulty)
  c.showPage()
# Save and close the PDF
c.save()
print("PDF created")
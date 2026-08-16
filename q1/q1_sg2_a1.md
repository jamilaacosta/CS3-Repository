Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9-Samat Score:__________

C# / Name: 16-TRIA, 17-ABLOLA, 18-ACOSTA Date: 08/16/2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: Students and teachers of Pisay CLC are held up in queues during their lunch break.  


Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

Possible subproblems:  
1. Not all students are quick to decide on what to order.  
2. The cashiers have to manually calculate the total, and change of each customer.  
3. The cashiers have no way to monitor on which food items need restocking.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

| Sub-problem | CT Skills | Example Solution |
| --- | --- | --- |
| Some students are indecisive on what to eat. | Pattern Recognition | Present a menu for students to decide what to eat beforehand. |
| Cashiers have to manually calculate orders and change | Decomposition | Provide calculators to the cashiers; lessening the burden from them manually subtracting or adding orders to just inputting numbers into a calculator. |
| Cashiers cannot monitor items that need restocking | Algorithm Design | Before the transaction finalizes, cashiers first have to log what item a customer buys into a spreadsheet. Therefore, in some way, cashiers can keep track of which items maybe running low on stock. |


 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
 ![My flowchart](../images/flowchart.PNG "My flowchart")

```mermaid
graph TD
  A([START]) --> B[Sub-problem; Cashiers cannot monitor items that need restocking] 
  B --> C[/Sell item/s to customer/] 
  C --> D{/Did the customer buy more than one item?/} 
  D -- No -->E[Simply log the item bought into the spreadsheet.] 
  E --> F([END])

  D -- Yes --> G[Take into account how the quantity of each item/s the customer bought into spreadsheet] 
  G --> H[Log into the spreadsheet] 
  H --> F([END])

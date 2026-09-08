# AI Agents

## 1. What is an Agent?

An **Agent** is a software system that can **perceive its environment, make decisions, and take actions to achieve a goal**.

In the context of AI, an Agent usually uses an **LLM (Large Language Model)** as its reasoning component.

A simple definition:

> **An AI Agent is an LLM-based system that can reason about a goal, use tools, take actions, observe the results, and continue until the task is completed.**

For example, if we ask a normal LLM:

```text
What is the weather in London?
```

The LLM can generate an answer based on its available knowledge.

An Agent, however, could:

1. Understand the request.
2. Decide that it needs current weather data.
3. Call a weather API.
4. Receive the result.
5. Interpret the result.
6. Return the answer to the user.

---

# 2. LLM vs Agent

An **LLM is not necessarily an Agent**.

An LLM primarily generates text based on its input.

```text
User Input
    ↓
   LLM
    ↓
Generated Response
```

An Agent adds additional components around the LLM:

```text
User
  ↓
Agent
  ↓
LLM
  ↓
Decision
  ↓
Tool / Action
  ↓
Observation
  ↓
LLM
  ↓
Final Response
```

The important difference is that an Agent can create a **loop of reasoning and action**.

---

# 3. The Agent Loop

A common Agent architecture follows this cycle:

```text
Goal
  ↓
Observe
  ↓
Reason
  ↓
Act
  ↓
Observe Result
  ↓
Reason
  ↓
Act
  ↓
...
  ↓
Finish
```

This is often called the **Agent Loop**.

### Example

Suppose the user says:

```text
Find the cheapest flight from Tehran to Berlin next week.
```

The Agent might do:

```text
Understand request
      ↓
Determine required information
      ↓
Search flight APIs
      ↓
Compare prices
      ↓
Check dates
      ↓
Select cheapest option
      ↓
Return result
```

The Agent decides which actions are necessary instead of simply generating a static response.

---

# 4. Main Components of an Agent

A typical AI Agent contains several components.

```text
                ┌──────────────┐
                │     User     │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │    Agent     │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │     LLM      │
                └──────┬───────┘
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Tools          Memory        State
        ↓              ↓              ↓
     APIs          Context       Progress
        ↓
    External
    Systems
```

The most important components are:

* **LLM**
* **Tools**
* **Memory**
* **State**
* **Planning / Reasoning**
* **Environment**
* **Actions**

---

# 5. LLM

The **LLM** is usually the reasoning and language component of an Agent.

Examples include:

* GPT
* Claude
* Gemini
* Llama

The LLM can help the Agent:

* Understand user requests
* Interpret information
* Decide what to do next
* Select tools
* Generate arguments for tools
* Analyze tool results
* Produce the final response

However, the LLM itself does not automatically make a complete Agent.

The Agent is the **system built around the LLM**.

---

# 6. Tools

A **Tool** is an external capability that an Agent can use to perform an action or obtain information.

Examples:

```text
Web Search
Database
Calculator
Weather API
File System
Email API
Calendar API
Python
Code Execution
Payment API
```

For example:

```text
User:
"Calculate the average temperature of these cities."

Agent:
"I need the temperature data."

        ↓

Weather Tool
        ↓

Temperature Data

        ↓

Calculator
        ↓

Average Temperature

        ↓

Final Answer
```

Tools allow Agents to interact with systems outside the LLM.

---

# 7. Function Calling / Tool Calling

LLMs can be given access to structured tools.

For example, an Agent may have:

```json
{
  "name": "get_weather",
  "description": "Get the current weather",
  "parameters": {
    "city": "string"
  }
}
```

The model can decide:

```text
I need current weather information.
```

Then it generates a tool call such as:

```json
{
  "city": "Berlin"
}
```

The application executes the function:

```python
weather = get_weather("Berlin")
```

The result is then returned to the LLM.

```text
LLM
 ↓
Tool Call
 ↓
Application
 ↓
Tool
 ↓
Result
 ↓
LLM
```

This mechanism is one of the foundations of modern AI Agents.

---

# 8. Environment

The **Environment** is everything outside the Agent that it can interact with.

For example:

```text
Agent
  │
  ├── Web
  ├── Database
  ├── File System
  ├── APIs
  ├── Applications
  └── External Services
```

The Agent receives information from the environment and can perform actions within it.

---

# 9. Actions

An **Action** is something the Agent does.

Examples:

```text
Search the web
Read a file
Write a file
Send an email
Query a database
Call an API
Create a calendar event
Execute code
```

A useful abstraction is:

```text
Observation → Decision → Action
```

For example:

```text
Observation:
The database contains 0 records.

Decision:
Create a new record.

Action:
INSERT record into database.
```

---

# 10. Memory

Agents may need to remember information.

Memory can be divided into different types.

## Short-Term Memory

Short-term memory contains information from the current interaction.

For example:

```text
User:
My name is Alex.

User:
What is my name?
```

The Agent can use the conversation context to answer:

```text
Your name is Alex.
```

---

## Long-Term Memory

Long-term memory stores information that can be used across different sessions.

For example:

```text
User Preferences
        ↓
Database / Vector Database
        ↓
Future Agent Session
```

The Agent can retrieve relevant information when needed.

---

# 11. State

**State** represents the current condition or progress of an Agent.

For example, an Agent working on a travel booking task might have:

```json
{
  "destination": "Berlin",
  "departure_date": "2026-10-10",
  "return_date": "2026-10-20",
  "flight_selected": false
}
```

As the Agent performs actions, the state changes:

```text
flight_selected: false
        ↓
Search Flights
        ↓
Compare Flights
        ↓
flight_selected: true
```

State is especially important for long-running or multi-step Agents.

---

# 12. Planning

Some tasks require multiple steps.

For example:

```text
"Research three laptops, compare their specifications,
and recommend the best one for programming."
```

An Agent might create a plan:

```text
1. Search for laptops.
2. Collect specifications.
3. Compare CPUs.
4. Compare RAM.
5. Compare storage.
6. Compare prices.
7. Determine the best option.
8. Generate the final answer.
```

Planning allows the Agent to break a complex goal into smaller tasks.

---

# 13. Reasoning

The Agent needs to determine what action should happen next.

Conceptually:

```text
Current State
     ↓
Reasoning
     ↓
Next Action
```

For example:

```text
Goal:
Find the latest Bitcoin price.

Current information:
No current price available.

Reasoning:
The model needs external data.

Next Action:
Call a cryptocurrency price API.
```

The exact internal reasoning of modern models should not be confused with the overall Agent architecture. From an engineering perspective, what matters is the **decision → action → observation** cycle.

---

# 14. Agent Example

Consider an Agent that manages emails.

The user says:

```text
Find emails from John about the project
and summarize them.
```

The Agent could perform:

```text
User Request
     ↓
Understand Task
     ↓
Search Email
     ↓
Retrieve Emails
     ↓
Filter Relevant Messages
     ↓
Summarize Content
     ↓
Return Summary
```

The Agent may use:

```text
LLM
 ↓
Email Search Tool
 ↓
Email Data
 ↓
LLM
 ↓
Summary
```

The important point is that the LLM does not need to directly access the email system.

The **Agent runtime** connects the LLM to the email tool.

---

# 15. Agent Architecture

A simplified production architecture can look like this:

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │  Agent Runtime│
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │      LLM      │
                    └───────┬───────┘
                            ↓
                    ┌───────────────┐
                    │ Decision/Plan │
                    └───────┬───────┘
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
           Search        Database        Python
            Tool           Tool           Tool
              ↓             ↓             ↓
              └─────────────┼─────────────┘
                            ↓
                       Observation
                            ↓
                           LLM
                            ↓
                      Final Response
```

---

# 16. Agent vs Chatbot

A traditional chatbot might work like:

```text
User
 ↓
LLM
 ↓
Response
```

An Agent can work like:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Another Tool
 ↓
Result
 ↓
Final Response
```

Therefore:

| Feature              |   Basic Chatbot | AI Agent |
| -------------------- | --------------: | -------: |
| Generate text        |               ✓ |        ✓ |
| Understand context   |               ✓ |        ✓ |
| Use tools            |       Sometimes |        ✓ |
| Take actions         |         Limited |        ✓ |
| Multi-step tasks     |         Limited |        ✓ |
| External systems     |         Limited |        ✓ |
| Planning             | Usually limited |        ✓ |
| Autonomous execution |      Usually no |    Often |

The boundary is not absolute. A chatbot can have tools, and an Agent can be highly constrained.

---

# 17. Agent vs LLM

It is useful to remember:

```text
LLM ≠ Agent
```

An LLM is a model.

An Agent is a **system** that can use an LLM together with tools, state, memory, and an execution loop.

A simplified relationship:

```text
              AI Agent
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
      LLM      Tools     State
                 │
              Memory
```

---

# 18. Single-Agent Systems

A **Single-Agent System** uses one Agent to perform a task.

Example:

```text
User
 ↓
Research Agent
 ↓
Search Tool
 ↓
Database Tool
 ↓
LLM
 ↓
Answer
```

This is usually the simplest architecture and is a good starting point for an MVP.

---

# 19. Multi-Agent Systems

A **Multi-Agent System** contains multiple specialized Agents.

For example:

```text
                    Manager Agent
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    Research Agent   Coding Agent   Testing Agent
          │              │              │
       Search          Python          Test Tool
```

Each Agent can have a specific responsibility.

Example:

```text
Manager:
"Build a small web application."

Research Agent:
Research requirements.

Coding Agent:
Write the code.

Testing Agent:
Run tests.

Manager:
Review results and finish the task.
```

However, multi-agent architectures introduce significant complexity.

For an MVP, a single Agent with well-designed tools is often preferable.

---

# 20. Tool Selection

One of the important responsibilities of an Agent is deciding **which tool to use**.

Suppose the Agent has:

```text
Tools:
- calculator
- web_search
- database
- email
```

User:

```text
What is 25 × 48?
```

The Agent should select:

```text
calculator
```

User:

```text
Find my emails from yesterday.
```

The Agent should select:

```text
email
```

This can be represented as:

```text
User Request
     ↓
     LLM
     ↓
Choose Tool
     ↓
Execute Tool
     ↓
Observe Result
```

---

# 21. The Agent Runtime

The **Agent Runtime** is the software responsible for executing the Agent's workflow.

It may handle:

* Sending prompts to the LLM
* Managing tool calls
* Executing tools
* Maintaining state
* Handling errors
* Managing memory
* Controlling loops
* Setting execution limits
* Logging
* Authentication
* Permissions

A simplified runtime:

```python
while not finished:

    response = llm(state, tools)

    if response.requires_tool:
        result = execute_tool(response.tool)
        state.add(result)

    else:
        return response
```

This is a simplified conceptual example, not a complete production implementation.

---

# 22. Error Handling

Agents interact with external systems, so failures are expected.

For example:

```text
Agent
 ↓
Weather API
 ↓
Timeout
```

A production Agent should handle this.

Possible strategies:

```text
Tool fails
   ↓
Retry
   ↓
Still fails?
   ↓
Use another method
   ↓
Still unavailable?
   ↓
Tell the user
```

Agents should not assume that every tool call succeeds.

---

# 23. Guardrails

Agents can potentially perform real actions.

For example:

```text
Send Email
Delete File
Modify Database
Make Payment
Deploy Application
```

Therefore, production Agents need **guardrails**.

Examples:

```text
Permission checks
Input validation
Tool restrictions
Rate limits
Maximum execution steps
Human approval
Sandboxing
Audit logs
```

For example:

```text
Agent:
"I want to delete 5,000 records."

System:
"This action requires human approval."

       ↓

Human Approval

       ↓

Execute Action
```

---

# 24. Autonomy

Agent autonomy exists on a spectrum.

### Low Autonomy

```text
User → Agent → Tool → User
```

The user controls most decisions.

### Medium Autonomy

```text
User → Agent → Multiple Tools → Result
```

The Agent can perform several actions automatically.

### High Autonomy

```text
Goal
 ↓
Agent
 ↓
Plan
 ↓
Many Actions
 ↓
Evaluate
 ↓
Modify Plan
 ↓
Continue
```

Higher autonomy generally means higher engineering and safety requirements.

---

# 25. A Practical Agent Example

Imagine building a **GitHub Issue Agent**.

User:

```text
Analyze issue #125 and fix the bug.
```

The Agent could:

```text
1. Read issue #125
2. Understand the bug
3. Inspect the repository
4. Search relevant files
5. Modify the code
6. Run tests
7. Analyze failures
8. Fix the code
9. Run tests again
10. Prepare a pull request
```

Tools might include:

```text
GitHub API
File System
Code Search
Python
Test Runner
Git
```

Architecture:

```text
                 User
                   ↓
              Agent Runtime
                   ↓
                  LLM
                   ↓
                Planner
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     GitHub      Files       Tests
       Tool       Tool        Tool
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
                Results
                   ↓
                  LLM
                   ↓
              Final Action
```

---

# 26. Important Terms

| Term              | Meaning                                               |
| ----------------- | ----------------------------------------------------- |
| **Agent**         | System that can reason and take actions toward a goal |
| **LLM**           | Language model used for understanding and generation  |
| **Tool**          | External capability available to the Agent            |
| **Tool Calling**  | Mechanism for an LLM to request execution of a tool   |
| **Environment**   | External systems the Agent interacts with             |
| **Action**        | Operation performed by the Agent                      |
| **Observation**   | Information returned after an action                  |
| **Memory**        | Information retained for future use                   |
| **State**         | Current data and progress of the Agent                |
| **Planning**      | Breaking a goal into multiple steps                   |
| **Agent Loop**    | Repeated observe → reason → act cycle                 |
| **Guardrail**     | Restriction or safety mechanism                       |
| **Agent Runtime** | System that executes and manages the Agent            |

---

# 27. The Core Mental Model

The most useful mental model for understanding Agents is:

```text
             ┌──────────────┐
             │     Goal     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │   Observe    │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │    Reason    │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │     Act      │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │   Observe    │
             └──────┬───────┘
                    ↓
                Continue
                    │
                    ↓
                  Finish
```

In short:

```text
Agent = Model + Tools + State + Execution Loop
```

A more complete production view is:

```text
Agent
│
├── LLM
├── Tools
├── Memory
├── State
├── Planning
├── Execution Loop
├── Guardrails
└── Observability
```

---

# 28. Key Takeaway

An Agent is **not simply a smarter chatbot**.

It is a software system that gives a model the ability to:

```text
Understand a goal
      ↓
Decide what to do
      ↓
Use tools
      ↓
Observe results
      ↓
Update its state
      ↓
Take another action
      ↓
Complete the goal
```

The LLM provides much of the language understanding and decision-making capability, while the surrounding software provides **tools, state, memory, execution, permissions, and control**.

That distinction is important when designing real-world Agent systems.

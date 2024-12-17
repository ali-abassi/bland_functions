# Welcome to Bland AI

Bland AI is a platform for AI phone calling that enables sending and receiving calls with programmable voice agents.

## Core Features
- **Fast**: Sub-second latency for AI responses
- **Reliable**: Enterprise-grade uptime and call quality
- **Flexible**: Configurable voice, transfers, greetings and behaviors

## Key Capabilities
- Send outbound AI phone calls
- Set up inbound phone numbers
- Connect external APIs during calls
- Extract structured data from conversations  
- Run large-scale call campaigns
- Fine-tune custom LLMs (Enterprise)

## Getting Started
- [API Reference](https://docs.bland.ai/api-v1)
- [Starter Guide](https://docs.bland.ai/starter-guide) 
- [Get API Keys](https://app.bland.ai/)
- [Enterprise Solutions](https://forms.default.com/361589)

## Documentation
- [Custom Tools](https://docs.bland.ai/tutorials/custom-tools)
- [Webhooks](https://docs.bland.ai/tutorials/webhooks)
- [Live Transfer](https://docs.bland.ai/tutorials/live-transfer)
- [Batch Calling](https://docs.bland.ai/tutorials/send-1000-calls-at-once)
- [Dynamic Data](https://docs.bland.ai/tutorials/dynamic-data)

## Support
- [Discord Community](https://discord.gg/QvxDz8zcKe)
- [Email Support](mailto:hello@bland.ai)

Title: Starter guide - Bland AI

URL Source: https://docs.bland.ai/starter-guide

Markdown Content:
Starter guide - Bland AI
===============
  

[Bland AI home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/blandai/logo/light.svg)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/blandai/logo/dark.svg)](https://docs.bland.ai/)

Search or ask...

*   [GET YOUR KEYS](https://app.bland.ai/)
*   [Support](mailto:hello@bland.ai)
*   [GET YOUR KEYS](https://app.bland.ai/)

Search...

Navigation

Get Started

Starter guide

[Documentation](https://docs.bland.ai/welcome-to-bland)[V1 API Reference](https://docs.bland.ai/api-v1/post/calls-simple)

*   [Community & Support](https://discord.gg/QvxDz8zcKe)
*   [Blog](https://www.bland.ai/blog)
*   [AMHLB Prompting Guide](https://docs.google.com/document/d/19JVeaM3c9a0JzsjsnzaZ2BOoBve4IeWx-fARDAgaEm8/edit)
*   [Full Code Examples](https://github.com/Bland-AI/Bland-AI-Cookbooks/tree/main)
*   [Zapier No-code integration](https://zapier.com/apps/bland-ai/integrations)
*   [Enterprise inquiries](https://forms.default.com/361589)

##### Get Started

*   [Welcome to Bland AI](https://docs.bland.ai/welcome-to-bland)
*   [Starter guide](https://docs.bland.ai/starter-guide)

##### Bland Enterprise

*   [Custom Twilio Integration](https://docs.bland.ai/enterprise-features/custom-twilio)
*   [Fine-tuning & Custom LLMs](https://docs.bland.ai/enterprise-features/custom-llm)
*   [Custom languages & voices](https://docs.bland.ai/enterprise-features/custom-tts)
*   [Bring your own Twilio](https://docs.bland.ai/enterprise-features/bring-your-own-twilio)
*   [Enterprise rate limits](https://docs.bland.ai/enterprise-features/enterprise-rate-limits)

##### Featured guides

*   [Bland & Botpress](https://docs.bland.ai/featured-guides/bland-and-botpress)

##### Basic Tutorials

*   [Conversational Pathways](https://docs.bland.ai/tutorials/pathways)
*   [Custom Tools](https://docs.bland.ai/tutorials/custom-tools)
*   [Send your first phone call](https://docs.bland.ai/tutorials/send-first-call)
*   [Webhook Signing](https://docs.bland.ai/tutorials/webhook-signing)
*   [Send 1000 phone calls](https://docs.bland.ai/tutorials/send-1000-calls-at-once)
*   [Dynamic Data](https://docs.bland.ai/tutorials/dynamic-data)
*   [Setting max duration](https://docs.bland.ai/tutorials/max-duration)
*   [Live transfer](https://docs.bland.ai/tutorials/live-transfer)
*   [Webhooks](https://docs.bland.ai/tutorials/webhooks)

# Starter Guide

Learn how to use Bland's API in under five minutes.

## Creating a Developer Account
1. Sign up at [developer portal](https://app.bland.ai/)
2. Enter phone number and verification code
3. Navigate to "Send phone call" page

## Sending Your First Call
The send phone call page provides a testing interface:
1. Enter your phone number
2. Write a prompt or select an example
3. Click "Send call" button ($0.12/minute, billed per second)

For programmatic calls, see the [API reference](https://docs.bland.ai/api-v1/post/calls).

## Testing Your Phone Agent
Test and improve your agent using:
1. Direct test calls to yourself
2. Bland AI testing suite:
   - Configure model and language
   - Test edge cases through messaging
   - Refine prompt based on responses

## Next Steps
Explore advanced features:
- [API Reference](https://docs.bland.ai/api-v1)
- [Custom Tools](https://docs.bland.ai/tutorials/custom-tools) 
- [Prompting Guide](https://www.bland.ai/blog/prompting-guide-ai-phone-calls)
- [Community](https://discord.com/invite/8xGGg2KfH7)

# Custom Twilio Integration

Enterprise customers can connect their own Twilio account to Bland, allowing them to use existing phone numbers and integrations.

## Prerequisites
- Your own Twilio account

## Step 1: Create Encrypted Key
1. Get Account SID and Auth Token from [Twilio Console](https://www.twilio.com/console)
2. Generate `encrypted_key` via [API request](https://docs.bland.ai/api-v1/post/accounts)

**Important**: Store the `encrypted_key` securely - it's only shown once and new keys must be generated if lost.

## Step 2: Use Key for Outbound Calls
Include `encrypted_key` in API request headers (along with `Authorization`). Notes:
- Set `from` number owned by your Twilio account
- Default: Random number from your Twilio account if `from` not specified

## Step 3: Upload Inbound Numbers
1. Get phone numbers from [Twilio Console](https://www.twilio.com/console)
2. Upload via [API](https://docs.bland.ai/api-v1/post/inbound-insert)

Numbers are validated against your account before being added.

## Step 4: Configure Numbers/Webhooks
- Include `encrypted_key` in headers when updating inbound numbers
- Update numbers through [Dev Portal](https://app.bland.ai/) or [API](https://docs.bland.ai/api-v1/post/inbound-number-update)
- Numbers automatically configured on Bland infrastructure

# Fine-tuning & Custom LLMs

Enterprise customers can fine-tune custom models using their call transcripts and host them on Bland's infrastructure for sub-second latency.

## Summary
- Fine-tune models using your successful call transcripts
- Host models on dedicated infrastructure 
- Connect existing custom LLMs to reduce latency
- Contact us [here](https://forms.default.com/361589)

## Background
Traditional AI phone agents use models from:
- OpenAI, Anthropic etc.
  - Good at following instructions
  - High quality outputs
  - But slow and limited personality/tone
  - Uptime and security concerns

Open source models:
- Generally lower performance
- But can be fine-tuned for specific tasks
- Can exceed GPT-4 capabilities when specialized

## How to Fine-tune
[Contact the Bland team](https://forms.default.com/361589) to discuss:
1. Required data format
2. Timeline (typically 1 week)
3. Pricing (typically under $10k)

# Custom Languages & Voices

Enterprise customers can customize voice and language capabilities:

## Custom TTS Options
- Bring your own Text-to-Speech service
- Work with Bland engineering for high-quality voice clones
- Configure custom voices to match your brand

## Foreign Language Support
Available languages include:
- German
- Spanish 
- Italian
- Portuguese

Bland's engineering team will configure:
- Language-specific transcription
- Appropriate TTS models
- Full localization support

## Getting Started
[Contact us](https://forms.default.com/361589) to discuss:
1. TTS requirements and voice preferences
2. Language needs
3. Integration timeline and setup

# Bring Your Own Twilio

Enterprise customers can create and connect their own Twilio account to Bland.

## Features
- Full ownership of telephony infrastructure
- Ability to connect to existing telephony infrastructure 
- Closer control of spam risk
- Leverage existing discounted rates on your account

## Benefits
By bringing your own Twilio account, you get:
- Complete control over your telephony setup
- Seamless integration with existing systems
- Maintain existing pricing and relationships
- Enhanced security and compliance options

## Getting Started
[Contact us](https://forms.default.com/361589) to learn more about:
1. Account setup and integration
2. Migration process
3. Technical requirements

# Enterprise Rate Limits

## Default Limits
By default, Bland customers can dispatch 1000 calls/day before hitting rate limits.

## Enterprise Capacity 
Enterprise customers receive significantly higher limits:
- 20,000 calls per hour
- 100,000 calls per day

[Contact us](https://forms.default.com/361589) to discuss enterprise rate limits and custom capacity needs.

# Bland & Botpress

## Overview
The integration process involves several key steps, starting with setting up your Botpress server and configuring your Bland AI account to ensure both platforms can communicate effectively. You'll learn how to authenticate your Botpress instance with Bland AI, send dynamic data (like phone numbers and intents) from chatbot conversations to Bland AI, and initiate voice calls based on user inputs or specific triggers within your chatbot workflows. This guide is also a great way for no-coders to deploy a bland AI project easily, with little to no coding experience.

## What You'll Learn
This guide will cover:

- **Setting Up Botpress**: Instructions on preparing your Botpress environment for integration, including installation and basic configuration.

- **Configuring Bland AI**: How to set up your Bland AI account, obtain necessary API keys, and understand the API's capabilities related to voice interactions.

- **Integration Workflow**: Step-by-step guidance on creating workflows in Botpress that interact with Bland AI's API, focusing on initiating voice calls to user-provided numbers.

- **Testing and Troubleshooting**: Tips for testing your integrated solution to ensure it works as expected and troubleshooting common issues that may arise during the integration process.

- **Advanced Use Cases**: Ideas and examples for leveraging this integration to create innovative chatbot applications that blend chat and voice interactions in unique and valuable ways.

# Conversational Pathways
Gain greater control over your AI agent and the conversational flow. Create a Pathway Now!

[Template Pathway Video Tutorial]()

## Introduction
Conversational pathways are our new way of prompting Bland that has led to major breakthroughs in realism.

### Greater dialogue control
Give your agent instructions on how it should respond at specific points of the conversation. Choose between prompting or fixed sentences.

### Webhooks
Execute webhooks at any point during the conversation, and send speech during/after the webhook.

### End call
Control when your agent ends the call

### Knowledge Base
Connect your agent to a knowledge base, to answer any questions the user has.

## Terminologies
To understand how pathways work, let's first understand the terminologies.

### Nodes
These blocks you see here are called Nodes.

### Pathways
Each of these dotted lines is called a Pathway. Their start end end points are the Purple Circles on the top and bottom of the nodes.

In order to create a pathway from a node, you would click on the purple circle at the bottom of the node and drag your mouse to connect to the top purple circle another node.

Upon doing so, you will now have a new dotted line connecting the two nodes, with a 'New Pathway' button in the middle of the line.

In order to instruct the agent when to take this pathway, you would click on the Edit icon on the 'New Pathway' button, and input the conditions for when the agent should take this pathway. In the above example, the agent would take this pathway if the user is not available to talk, so I labelled the pathway as 'not a good time to talk'.

And there you have it! You have now created a pathway from one node to another, and instructed the agent when to take this pathway. You can connect as many nodes as you want in this manner, and create as many pathways as you want. In order to create a new Node, press the 'Add new Node' button at the top-left of the screen.

## How the Pathways Agent Works
The agent starts at the first node, and then moves to the next node based on the pathway that the agent decides to take. The agent will then execute the instructions in the node as dialogue, and then move on to the next node based on the pathway that the agent decides to take. This process will continue until the agent decides to end the call.

The agent will make decisions based on the labels you put in the pathways, when connecting one node to another, and the dialogue generated will be based on the instructions you set in the nodes.

### For Example
In this example, at the node named 'Ask for reservation info', the node asks for the user's reservation information. Based on the user's response, the agent will then move on to the next node based on the labels you put in the pathways. For the current node, it will check if the user has provided reservation information where the number of guests is either less than 8 or more than 8. If the user has provided reservation information where the number of guests is less than 8, the agent will move on to the node named 'Reservation booking'. If the user has provided reservation information where the number of guests is more than 8, the agent will move on to the node named 'Transfer Call'. The agent will then execute the instructions in the node as dialogue, and then move on to the next node based on the pathway that the agent decides to take. And the process repeats!

## Conditions
Conditions are a way to provide the agent with a condition that must be met in order for the agent to move on to the next node. If the condition is not met, the agent will stay on the same node and ensure the condition is met until the condition is fulfilled.

Using the same example above, I set the condition for the 'Ask for reservation info' node as follows - "You must get the date, time, and number of guests for this reservation". This means that the agent will stay on the 'Ask for reservation info' node until the user provides the date, time, and number of guests for the reservation. If the user says something else or deviates from the conversation, the agent will stay on the 'Ask for reservation info' node and prompt the user to provide the date, time, and number of guests for the reservation.

This helps you to ensure that the user provides the necessary information before moving on to the next node, and helps you to control the flow of the conversation.

## Global Nodes
Global Nodes take precendence over the condition decisions made by the agent. You can treat a global node as a node, that every other node in the pathway has a pathway to, with the label as the 'Global Pathway Label'.

Using the Reservation Booking Example, if the user were to ask a question like 'What are the opening hours of the restaurant' when the agent is at the 'Ask for reservation info' node, the condition decision would not be met as the user did not provide the date, time, and number of guests for the reservation. However, the pathway label would be 'user has a question about the restaurant's hours or location', which links to a Global Node. As Global Nodes take precedence over the condition decision, the agent would then move to the 'Global Node' named 'Restaurant Questions' and provide the user with the opening hours of the restaurant. After providing the user with the opening hours of the restaurant, the agent would then automatically return to the 'Ask for reservation info' node, and continue with the flow of the conversation.

This helps you to handle edge cases where the user might ask a question that is not related to the current conversation, and allows you to provide the user with the information they need, before returning to the conversation.

Tip: The variables {{lastUserMessage}} and {{prevNodePrompt}} can be used in the Global Node to provide the agent with context on what the user said, and steering the conversation back to its own original goal.

Example Global Node Prompt:

## Node Types
There are currently 6 different types of Nodes:

- Default
- Webhook  
- Knowledge Base
- End Call
- Transfer Call
- Wait for Response

You can select the type of node you want by clicking on the dropdown of Node Type.

## Base/Default Node (Important!)
The default node provides the ability to generate a response to the user. This functionality is exposed to all other nodes as well.

You can either:

- Use the Prompt field to give instructions on what the agent should do at this point in the conversation. This is the recommended way to generate responses as it makes the conversation more human and natural.
- Enable the 'Static Text' toggle to provide a fixed response, and the agent will always say the same thing at this point in the conversation.

## Optional Decision Guide
The optional decision guide is only to be used if your phone agent currently is not going down the correct pathway. We do not expect this to happen often, but still want to provide you the tools to handle these issues if they arise.

It is a way to provide the phone agent with example scenarios of what the user might say, and what pathway the agent should take in response.

You would put in examples of what the user might say in the User Input field, and then in the Pathway field, you would provide the pathway the agent should take in response.

## Condition
The condition is a way to provide the agent with a condition that must be met in order for the agent to move on to the next node. If the condition is not met, the agent will stay on the same node and ensure the condition is met until the condition is fulfilled.

## Global Nodes
Each node can be configured to be a Global Node. Global Nodes are nodes that are accessible by every other node in the Conversational Pathway. This means that it has an implicit pathway to every other node, and the label would be the 'Global Label'.

After entering a Global Node, the agent will execute the instructions inside the Global Node, and then automatically return to the node it was at before entering the Global Node, so it can continue with the flow of the conversation.

In a Global Node, you can also forward the agent to another node, by toggling the 'Enable Forwarding', which will allow you to select the node you want to move the agent to. This is useful if you want to move the agent to a existing node for a certain scenario, which could happen at any point in the conversation.

## Transfer Call Node
The transfer call node is used to transfer the call to another number when the node is reached, and the dialogue at this node is complete.

As such, you may have the agent say any final words before the call is transferred.

## End Call Node
The end call node will end the call when the node is reached, and the dialogue at this node is complete.

As such, you may have the agent say any final words before the call is ended.

## Knowledge Base Node
The knowledge base node is used to connect your agent to a knowledge base, to answer any questions the user has.

Paste in any text in the 'Knowledge Base' field, and the agent will search through the knowledge base to answer the user.

Coming soon - PDF Upload/Vector Database Integrations...

## Wait for Response Node
The Wait for Response Node works the same way as the Default Node, except it is also equipped with the ability to wait if the user requires time to respond or needs to hold for a moment.

## Webhook Node
The webhook node is used to execute webhooks at any point during the conversation, and send speech during/after the webhook.

Webhook Information is all you need in order to execute a webhook, and works the same way as Dynamic Data. Refer to the Dynamic Data section for more information...

Similar to how the dialogue is handled in all other nodes, you can control the dialogue sent before, and after the webhook is executed.

Variables received from the webhook can be used in the dialogue as well, as shown in the example below.

## Global Prompt for all Nodes
The 'Add Global Prompt to All Nodes' feature is to assist in providing context/instructions to the agent for all nodes, without having to manually input the same prompt for each node. One Example of a Global Prompt could be to provide the agent with instructions on how to handle the call, the tone of voice to use, or answering any questions the user might have.

## Live Call Logs
The live call logs are a way to provide you with a live feed of the conversation between the agent and the user. This is useful for debugging purposes, and to see how the agent is responding to the user in real-time and the decisions the agent is making. On top of the transcript, we expose the updated node the agent took, the pathway that the agent took, as well as whether the condition was met or not.

## Testing the Pathway Agent via Chat
You can test the responses from your pathway agent by clicking on the 'Chat with Pathway' button at the top right of the screen. This will open a chat window where you can test the agent by sending messages to the agent, and see how the agent responds. The live call logs will also be displayed on the right side of the screen, so you can see the decisions the agent is making in real-time.

## Variables Reference/ Extraction

### Variables
You can reference variables in pathways using double curly braces like {{first_name}}. You can pass variables into your call by passing in the key-value pairs in the request_data field when sending a call.

Some examples of variables that you can access at each node:

- {{lastUserMessage}} - The last response from the user
- {{prevNodePrompt}} - The prompt from the previous node
- {{now_utc}} - The current time in UTC
- {{from}} - The phone number the call is from
- {{to}} - The phone number the call is to
- {{call_id}} - The unique identifier for the call

### Extracting Variables from Call/User Response
At each node, you can also extract variables from the user's response using the Extract Variables from Call Info field. You would put in the name of the variable you want to extract, the type of the variable (integer, string, boolean), and the description for what information you want the variable to store. You can also provide specific formats you expect and examples in the description. The more descriptive it is, the better the agent will be at extracting the variable more accurately.

Do note that when enable variable extraction, and wanting to reference the variable in the subsequent nodes, it would introduce slight latency as the agent would have to extract the variable from the user's response before generating the dialogue for the next node.

Within the webhook node, the variable extraction happens before the webhook is executed, so that you can reference the variables extracted from the user's response in the webhook's request data. The variables extracted from the webhook in response_data can also be referenced in the dialogue generated after the webhook is executed, in the same manner.

For Example, the image below shows how the Webhook Node is set up to extract the date, time, and number of guests for the reservation, and how the extracted variables are referenced in the webhook's request data.

## Fine Tuning the Pathway agent
While Conversational Pathways gives you a lot greater control compared to the regular call agent, hallucinations can still occur, or the agent might make wrong decisions in the pathway. However, we have provided you with the tools to handle these issues if they arise. Each node can be fine-tuned on the decision it makes, as well as the expected dialogue it generates, allowing you to handle even the most extreme edge cases that might arise easily.

### Steps to Fine-Tuning the agent
Upon triggering and testing a call with your pathway using the 'Chat with Pathway' button, or sending a call, you will be able to see the live call logs.

If you see a decision that the agent made that you do not agree with, or if the agent is hallucinating, you can fine-tune the decision the agent makes by clicking on the Edit button on the PATHWAY DECISION INFO block.

Upon doing so, you will be able to see the decisions the agent made for the condition, the pathway it took, and the dialogue it generated. You can then fine-tune the agent by changing the dialogue, the condition, or the pathway the agent took.

Upon saving your changes, you will be able to see the fine-tuning data in the node where the decision was made. This training data is used to train the agent to make better decisions in the future, and to ensure that the agent does not make the same mistake again.

Do note that the decisions for the condition and pathway chosen is made by the node the agent is currently at, and the dialogue is generated by the node which the agent decides to take the pathway to.

For Example, If the agent is at Node 1, and the agent decides that the condition is achieved, and decides to take the pathway to Node 2, the dialogue generated will be from Node 2, and the decisions for the condition and pathway chosen will be from Node 1. As such, the training data for the condition and pathway chosen will be stored in Node 1, and amendments to the dialogue generated will be stored in Node 2.

## Quick Start with Tutorial / Templates
To immediately start playing around with Conversational Pathways, you can use one of our templates. Visit the Conversational Pathways page on our Dev Portal, and duplicate the 'Restaurant Reservation' Template, and run through the agent to see how it works! We have also created a video walkthrough of that template to help you get started!

# Custom Tools

Interact with the real world mid-call using custom tools.

---

## Introduction

Custom tools allow your agent to interact with any web API mid-call. Do things like:

- **Send a message**: Dispatch SMS or emails using the person’s contact info.
- **Schedule an appointment**: Set appointments using live calendar availability.
- **Create a support ticket**: Generate support tickets in your issue tracker.
- **Update your CRM**: Update your CRM with relevant details during the call.

---

## Background

To understand how custom tools work, let’s take a peek under the hood of the Bland AI phone agent.

During the conversation, the phone agent is constantly listening to figure out when it’s supposed to respond. When the phone agent realizes it’s time to respond, it reviews the tools in its toolbox and picks between them.

Those tools include a speak, wait, and button press tool. When you create a custom tool, you add it to the existing ‘toolbox’ for the phone agent to pick from.

A few natural questions arise:

1. How do I define my custom tool?
2. How do I make sure my tool gets picked at the right time?
3. How does information from the call get passed to my custom tool’s API request?
4. How do I fill the silence (when my custom tool is running)?
5. How does the response from my custom tool get added to the call?

Keep reading to find out.

---

## Creating Your Custom Tool

### Custom Tool Example

```json
{
    "name": "BookAppointment",
    "description": "Books an appointment for the customer",
    "url": "https://your-api.com/book-appointment",
    "method": "POST",
    "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
    },
    "body": {
        "date": "{{input.date}}",
        "time": "{{input.time}}",
        "service": "{{input.service}}"
    },
    "input_schema": {
        "example": {
            "speech": "Got it - one second while I book your appointment for tomorrow at 10 AM.",
            "date": "2024-04-20",
            "time": "10:00 AM",
            "service": "Haircut"
        },
        "type": "object",
        "properties": {
            "speech": "string",
            "date": "YYYY-MM-DD",
            "time": "HH:MM AM/PM",
            "service": "Haircut, Coloring, Trim, or Other"
        }
    },
    "response": {
        "succesfully_booked_slot": "$.success",
        "stylist_name": "$.stylist_name"
    }
}
```

---

### From API Request to Custom Tool

Custom tools have the following properties:

- **name**: The agent will see this in the list of tools.
- **description**: A short explanation of what the tool does.
- **input_schema**: A JSON schema describing the input data.
- **speech (optional)**: A string that will be spoken to the agent while your tool waits for a response.
- **response_data**: An array of objects that describe how to extract data from the response. Variables created can be referenced in the prompt.

---

### Name & Description

The agent will see the name in the list of tools. The name, plus the description, help the AI phone agent when it decides which tool to use.

For this example, we’ll set the **name** to `BookAppointment` and the **description** to `Books an appointment for the customer`.

---

### Input Schema

The input schema defines the shape of the API request, the inputs it can take, and includes an example to assist with creating requests.

#### Example Input Schema:

```json
"input_schema": {
    "example": {
        "speech": "Got it - one second while I book your appointment for tomorrow at 10 AM.",
        "date": "2024-04-20",
        "time": "10:00 AM",
        "service": "Haircut"
    },
    "type": "object",
    "properties": {
        "speech": "string",
        "date": "YYYY-MM-DD",
        "time": "HH:MM AM/PM",
        "service": "Haircut, Coloring, Trim, or Other"
    }
}
```

**Notes:**
1. `input_schema` is converted into the variable `{{input}}` for use in the request body/query/headers.
2. Use dot notation to access nested properties, e.g., `{{input.service}}`.

---

### Speech

Define a **speech** property to fill silence while the API request processes.

**Example:**

> "Perfect, I'll schedule that right now, give me just a second."

---

### Response Data

Extract and make the phone agent aware of the response data using the `response_data` field.

#### Example Response Data:

```json
"response": {
    "succesfully_booked_slot": "$.success",
    "stylist_name": "$.stylist_name"
}
```

---

### Full Example

Below is the entire API request for sending a phone call using the outlined custom tool:

```json
{
    "phone_number": "+12223334444",
    "prompt": "...",
    "tools": [
        {
            "name": "BookAppointment",
            "description": "Books an appointment for the customer",
            "url": "https://your-api.com/book-appointment",
            "method": "POST",
            "headers": {
                "Authorization": "Bearer YOUR_API_KEY"
            },
            "body": {
                "date": "{{input.date}}",
                "time": "{{input.time}}",
                "service": "{{input.service}}"
            },
            "input_schema": {
                "example": {
                    "speech": "Got it - one second while I book your appointment for tomorrow at 10 AM.",
                    "date": "2024-04-20",
                    "time": "10:00 AM",
                    "service": "Haircut"
                },
                "type": "object",
                "properties": {
                    "speech": "string",
                    "date": "YYYY-MM-DD",
                    "time": "HH:MM AM/PM",
                    "service": "Haircut, Coloring, Trim, or Other"
                }
            },
            "response": {
                "succesfully_booked_slot": "$.success",
                "stylist_name": "$.stylist_name"
            }
        }
    ]
}
```

---

## Frequently Asked Questions

### How does the phone agent determine what it sends in an API request?

The phone agent refers to the `input_schema` and its example, which provide context about what data to pass. It extracts information from the transcript and uses it to populate the request body.

### How does the phone agent decide when to use the custom tool?

The agent looks at the tool’s name and description, then evaluates the current context of the conversation.

### How do I access the info the custom tool responds with?

Use `response_data` to extract variables from the API response. Once extracted, reference them in prompts using double brackets, e.g., `{{variable_name}}`.

**Example Prompt:**

> "You are taking a drive-thru order. Find out what the customer wants and repeat it back to confirm. Once confirmed, use the PlaceOrder tool and inform them of the order price: `{{order_price}}`."

---

If you have additional questions, reach out to **hello@bland.ai** for support.


# Send Your First Phone Call

---

## Step 1: Setup Your Authorization

Before making a call, you need to authenticate your request. Make sure you have your API key ready.

Sign up on the developer portal to get yours.

---

## Step 2: Prepare the Call Data

You will need to provide specific details for the call. These include:

- **phone_number**: The number you want to call. Remember to include the country code.
- **task**: Describe the purpose of the call and how the AI should handle the conversation.
- **voice_id**: Choose the voice persona (American male, Australian female, etc.) based on your preference.
- Set parameters like `reduce_latency`, `record`, `amd` (for navigating phone trees), and `wait_for_greeting` according to your call’s requirements.

---

## Step 3: Customize the Call

You can further personalize the call by:

- Setting a **first_sentence** for the call.
- Specifying **dynamic_data** to incorporate external API data.
- Adjusting **voice_settings** for stability, similarity, and speed.
- Choosing the language with the **language** parameter.
- Setting a **max_duration** for the call.

---

## Step 4: Send the API Request

Use the provided JavaScript or Python code snippet to make the API request.

### JavaScript Example:

```javascript
// Headers
const headers = {
  authorization: "YOUR-API-KEY-HERE",
};

// Data
const data = {
  phone_number: "+11233456789",
  task: "You are calling Fantastic Airlines on behalf of John Doe. Find out where John's Bags are located.",
  voice_id: 0,
  language: "eng",
  request_data: {
    calling: "Fantastic Airlines",
    bag_claim: "69683",
    airline_code: "UA123",
  },
  record: true,
  reduce_latency: true,
  amd: true,
};

// API request
await axios.post("https://api.bland.ai/v1/calls", data, { headers });
```

### Python Example:

```python
# Headers
headers = {
    'authorization': 'YOUR-API-KEY-HERE'
}

# Data
data = {
    'phone_number': '+11233456789',
    'task': "You are calling Fantastic Airlines on behalf of John Doe. Find out where John's Bags are located.",
    'voice_id': 0,
    'request_data': {
        'calling': 'Fantastic Airlines',
        'bag_claim': '69683',
        'airline_code': 'UA123'
    },
    'record': True,
    'reduce_latency': True,
    'amd': True
}

# API request
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)
```

---

## Step 5: Handle the Response

After the call, you will receive a response with the **status** and **call_id**. If you set `record` to `true`, you can retrieve the recording using the `/call/recording` endpoint.

### Example Response:

```json
{
  "status": "success",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1"
}
```

---

## Step 6: Monitor the Call

If you have set up a webhook, you will receive real-time notifications and transcripts once the call completes.

---

And that’s it! You’re now ready to make your first AI-powered phone call with Bland AI. Happy calling!

# Basic Tutorials: Webhook Signing

---

## Signing Webhooks

Bland webhooks are signed with a secret key to ensure that they are not tampered with in transit and to confirm that they were sent by Bland.

When Bland sends a webhook, it calculates a signature using the HMAC algorithm with the SHA-256 hash function. The signature is then included in the **X-Webhook-Signature** header of the request.

To create a webhook signing secret:
1. Go to **Account Settings** in the Dev Portal.
2. Click on the **Keys** tab.
3. Create a new secret by clicking **Replace Secret**. *(Note: The secret will only be shown once, so save it securely.)*

---

## Verifying Webhooks

To verify a webhook, calculate the HMAC signature of the request body using the secret key and compare it to the signature in the **X-Webhook-Signature** header.

> **Note:** You must first create a webhook signing secret in the Account Settings in the Dev Portal.

### Example: Verifying a Webhook in Node.js

```javascript
const crypto = require('node:crypto');

function verifyWebhookSignature(key, data, signature) {
	const expectedSignature = crypto.createHmac('sha256', key)
        .update(data)
        .digest('hex');
	
	return expectedSignature === signature;
}

//...

app.post('/webhook', (req, res) => {
    const isValid = verifyWebhookSignature(
        process.env.WEBHOOK_SECRET,
        JSON.stringify(req.body),
        req.headers['x-webhook-signature']
    );

    if (!isValid) {
        res.status(401).send('Invalid signature');
        return;
    }

    // Proceed with handling the webhook
    res.status(200).send('Webhook received');
});
```

# Basic Tutorials: Send 1000 Phone Calls

---

## Step 1: Setup Your Authorization

To initiate a batch call, you must first authenticate your request. Ensure you have your API key from signing up on the developer portal.

---

## Step 2: Create the Base Prompt

Craft a base prompt that will be common across all calls in the batch. Use placeholders `{{curly braces}}` for dynamic content.

**Example:**

```plaintext
"You are calling {{business}} to renew their subscription to {{service}} before it expires on {{date}}."
```

---

## Step 3: Define the Call Data

Specify the list of calls in the `call_data` array. Each call must have a `phone_number` and can include other properties corresponding to placeholders in your base prompt.

**Example:**

```json
[
  {
    "phone_number": "1234567890",
    "business": "ABC co.",
    "service": "Netflix",
    "date": "September 4th"
  },
  {
    "phone_number": "32176540987",
    "business": "XYZ inc.",
    "service": "Window Cleaning",
    "date": "December 20th"
  }
]
```

---

## Step 4: Additional Configuration

- **`label`**: Assign a label to your batch for easy tracking.
- **`campaign_id`**: Organize related batches under a campaign.
- **`test_mode`**: Set to `true` for testing with the first call only.
- **`batch_id`**: Manually set or auto-generated for tracking.
- **Voice and Language Settings**: Select `voice_id`, `reduce_latency`, and `language`.
- **`request_data`**: Include specific facts for the AI to know during the call.
- **`webhook`**: For real-time notifications and transcripts post-call.
- **`max_duration`**: Define the maximum length of each call.
- **`amd`**: Enable for navigating phone trees or leaving voicemails.
- **`wait_for_greeting`**: Control if the AI speaks immediately or waits.

---

## Step 5: Send the API Request

Use the provided JavaScript or Python code snippet to make the API request.

---

## Step 6: Handle the Response

After sending the batch request, you’ll receive a response with a `message` and the `batch_id`. Monitor the progress of your calls and any responses via your specified webhook.

**Example Response:**

```json
{
  "message": "success",
  "batch_id": "3p$7rQ3p9sT5bzmF-gen-batch"
}
```

---

## Step 7: Monitoring and Analytics

Track the performance and outcomes of your batch calls through the provided `batch_id` and campaign analytics. Adjust future batches based on the insights gained.

---

## Example Code: SendCalls.js

### JavaScript

```javascript
// Headers
const headers = {
  authorization: "YOUR-API-KEY-HERE",
};

// Data
const data = {
  base_prompt:
    "You are calling {{business}} to renew their subscription to {{service}} before it expires on {{date}}.",
  call_data: [
    {
      phone_number: "1234567890",
      business: "ABC co.",
      service: "Netflix",
      date: "September 4th",
    },
    {
      phone_number: "32176540987",
      business: "XYZ inc.",
      service: "Window Cleaning",
      date: "December 20th",
    },
  ],
  label: "Renewal Reminder - Wednesday Afternoon with female voice",
  voice_id: 0,
  max_duration: 10,
  reduce_latency: true,
  wait_for_greeting: true,
};

// API request
await axios.post("https://api.bland.ai/v1/batches", data, { headers });
```

---

# Basic Tutorials: Dynamic Data

---

## Introduction

With Dynamic Data, you can make external API requests at the start and throughout your phone call. This allows you to load data from your database, or from any other API. You can then use that data in your AI responses, or to define circumstantial behavior for each call.

### Examples of Dynamic Data Usage:

- Maintain conversation history between calls.
- Define behavior based on the user’s location.
- Handle real-time data like status updates or prices.

---

## System Variables

Variables are defined with double curly braces, like `{{variable}}`. System variables are predefined and available in every AI phone call. Use them to access information about the current call, such as the user’s phone number or the current time.

### Base Variables:

- `{{phone_number}}`: The other party’s number.
- `{{country}}`: The country code (e.g., US).
- `{{state}}`: The state or province abbreviation (e.g., CA for California).
- `{{city}}`: The full city name, capitalized.
- `{{zip}}`: The zip code.
- `{{call_id}}`: The unique ID of the current call.
- `{{now}}`, `{{now_utc}}`: Current time in local or UTC format.
- `{{from}}`, `{{to}}`: Outbound and inbound numbers in E.164 format.
- `{{short_from}}`, `{{short_to}}`: Numbers with country code removed.

**Example Usage:**

```json
{
    "task": "... Today is {{now}} ..."
}
```

---

## External API Requests

External API requests are defined in the `dynamic_data` parameter of your call request or inbound agent configuration. This parameter is an array of objects, where each object represents an API request.

### Example:

```json
{
    "dynamic_data": [
        {
            "url": "https://api.coindesk.com/v1/bpi/currentprice.json",
            "response_data": [
                {
                    "name": "bitcoin_price",
                    "data": "$.bpi.USD.rate",
                    "context": "Current price of Bitcoin in USD is ${{bitcoin_price}}"
                }
            ]
        }
    ]
}
```

---

## Extracting Data from Responses

Rather than using the full response, extract specific data using the `data` parameter. This follows JSON structuring with dot notation and array indices.

### Example Response:

```json
{
    "bpi": {
        "USD": {
            "code": "USD",
            "rate": "9,000.00",
            "description": "United States Dollar",
            "rate_float": 9000
        },
        "GBP": {
            "code": "GBP",
            "rate": "6,000.00",
            "description": "British Pound Sterling",
            "rate_float": 6000
        }
    }
}
```

`$.bpi.USD.rate` would return `9,000.00`.

---

## Variables as Parameters

Once defined with `response_data`, variables can be used almost anywhere:

- In the `task` or `prompt` parameters.
- In the `context` parameter of `response_data`.
- In the body, headers, and/or query parameters of each request.

Test configurations with the `/dynamic_data/test` endpoint, which returns the original configuration, raw responses, and parsed variables.

---

## Chaining Requests

Requests are executed sequentially, and variables from previous requests can be used in subsequent requests.

### Example:

1. **Retrieve Member ID:**

```json
{
    "dynamic_data": [
        {
            "url": "https://api.restaurant.com/customers",
            "method": "GET",
            "headers": {
                "authorization": "ExtremelySecureCredentials"
            },
            "query": {
                "phone_number": "{{phone_number}}"
            },
            "response_data": [
                {
                    "name": "member_id",
                    "data": "$.customer.member_id"
                }
            ]
        }
    ]
}
```

2. **Check Order Status:**

```json
{
    "dynamic_data": [
        {
            "url": "https://api.restaurant.com/orders",
            "method": "GET",
            "cache": false,
            "headers": {
                "authorization": "ExtremelySecureCredentials"
            },
            "query": {
                "member_id": "{{member_id}}"
            },
            "response_data": [
                {
                    "name": "order_id",
                    "data": "$.orders[0].id"
                },
                {
                    "name": "order_status",
                    "data": "$.orders[0].status"
                }
            ]
        }
    ]
}
```

# Setting Max Duration

---

## Introduction

Controlling the length of your AI-powered phone calls is crucial for efficiency and cost-effectiveness. In this guide, we’ll walk you through how to set a `max_duration` for your calls using Bland AI.

---

## Step 1: Understand max_duration

The `max_duration` parameter allows you to specify the longest duration you want your call to last, measured in minutes. Once the set duration is reached, the call will automatically end.

---

## Step 2: Setup Your Authorization

Ensure you have your API key ready for authentication. If you haven’t obtained one, sign up on the developer portal.

---

## Step 3: Define max_duration in Your Call Data

When preparing your call data, include the `max_duration` parameter. You can set it as a float or a string.

**Example Values:**
- "30"
- "5.5"
- 45
- 2.8

### Example Data:

```json
{
    "phone_number": "+11233456789",
    "task": "Inquire about the latest product updates.",
    "max_duration": "10" // Call lasts for 10 minutes max
}
```

---

## Step 4: Send the API Request

Use the provided JavaScript or Python code snippet to make the API request, ensuring you include the `max_duration` parameter.

### Python Example:

```python
# Headers
headers = {
    'authorization': 'YOUR-API-KEY-HERE'
}

# Data
data = {
    'phone_number': '+11233456789',
    'task': 'Inquire about the latest product updates.',
    'max_duration': '10', # Call lasts for 10 minutes max
}

# API request
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)
```

### JavaScript Example:

```javascript
// Headers
const headers = {
  authorization: "YOUR-API-KEY-HERE",
};

// Data
const data = {
  phone_number: "+11233456789",
  task: "Inquire about the latest product updates.",
  max_duration: "10", // Call lasts for 10 minutes max
};

// API request
await axios.post("https://api.bland.ai/v1/calls", data, { headers });
```

---

## Step 5: Test and Adjust

After setting `max_duration`, test your calls to ensure they’re ending at the desired time. Adjust as necessary based on your needs and feedback.

---

## Conclusion

Setting a `max_duration` for your calls ensures they are concise and to the point, saving time and resources. You’re now ready to efficiently manage the length of your AI-powered calls with Bland AI.

**Tip:** The key is to find the right balance between giving enough time for meaningful interaction and keeping the calls concise. Happy calling!


# Basic Tutorials: Live Transfer

---

## Introduction

Implementing live transfer in your AI-powered phone calls enhances flexibility and customer experience. This guide will explain how to set up a live transfer during a call using Bland AI.

---

## Step 1: Understand Live Transfer

Live transfer allows the AI agent to transfer the call to a human representative under certain conditions. This is crucial for scenarios where human intervention is preferred.

---

## Step 2: Setup Your Authorization

Before initiating a live transfer, ensure your API key is ready. Obtain your key from the developer portal if you haven’t already.

---

## Step 3: Configure the Transfer Settings

Include the `transfer_phone_number` parameter in your call data. This is the number the AI will transfer to. Additionally, define the conditions for transfer in the `task` parameter.

### Example:

```json
{
    "phone_number": "+11233456789",
    "transfer_phone_number": "+19876543210",
    "task": "If the caller requests to speak with a human, transfer the call to the representative."
}
```

---

## Step 4: Send the API Request

Make the API request using the JavaScript or Python code snippet provided, ensuring the `transfer_phone_number` and conditions are included.

### JavaScript Example:

```javascript
// Headers
const headers = {
  authorization: "YOUR-API-KEY-HERE",
};

// Data
const data = {
  phone_number: "+11233456789",
  transfer_phone_number: "+19876543210",
  task: "If the caller requests to speak with a human, transfer the call to the representative.",
};

// API request
await axios.post("https://api.bland.ai/v1/calls", data, { headers });
```

### Python Example:

```python
# Headers
headers = {
    'authorization': 'YOUR-API-KEY-HERE'
}

# Data
data = {
    'phone_number': '+11233456789',
    'transfer_phone_number': '+19876543210',
    'task': 'If the caller requests to speak with a human, transfer the call to the representative.'
}

# API request
response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)
```

---

## Step 5: Test and Monitor

After setting up the live transfer, test the functionality to ensure it works as expected. Monitor the calls to adjust the transfer conditions as necessary.

---

## Conclusion

Setting up a live transfer offers a seamless experience for situations where AI needs to hand over to a human. You’re now ready to integrate this feature into your AI-powered calls with Bland AI.

**Tip:** Maintain a balance between automated and human interactions to optimize customer satisfaction. Happy calling!

# Webhooks

---

## Introduction

This is a quick tutorial to help you set up and test your Bland AI webhook. We’ll include instructions both for inbound and outbound phone calls.

We’ll start with inbound because it’s more popular.

---

## Step 1: Create Your Webhook

To create a test webhook, visit [Webhook.site](https://webhook.site).

The website will automatically provide you with a unique webhook URL.

---

## Step 2: Connect to Your Inbound Phone Number

1. Open your developer portal and visit the inbound phone numbers page.
2. Paste your webhook into the webhook field. **Make sure to remove the initial `https://` when you insert the URL.**
3. Click **Test Webhook**.

---

## Step 3: Verifying Your Outputs

1. Navigate to the [Webhook.site](https://webhook.site) page.
2. Check if the test webhook fired correctly. You’ll know it worked because a new record will populate.

### Troubleshooting:
- If your record fails to populate, double-check that you provided the correct URL and removed the initial `https://`.
- If issues persist, join our Discord for immediate assistance from our team.

---

## Step 4: Test a Live Phone Call

1. Call your inbound phone number.
2. Once the call ends, visit the [Webhook.site](https://webhook.site) page again.
3. Confirm that a new record populated.

If this works, you’re all set!

---

## Step 5: Testing for Outbound Calls

1. Create your webhook by referring back to **Step 1**.
2. Follow the **Send Phone Call** documentation to create and send a phone call.
3. Include the webhook as a parameter in your request.
4. Confirm that the webhook data populated on your [Webhook.site](https://webhook.site) page.

### Troubleshooting:
- If you encounter issues, join our Discord and message us for help. Our team is ready to assist.

---


____________


# Basic
## Send Call (Simple)
Send an AI phone call with a custom objective and actions.

**POST**  
`/v1/calls`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name        | Type   | Required | Description                                          |
|-------------|--------|----------|------------------------------------------------------|
| phone_number| string | *        | Enter phone_number                                   |
| task        | string | *        | Enter task                                           |

---

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

---

### Body
#### phone_number
- **Type**: string  
- **Required**: Yes  
- **Description**: The phone number to call. Country code defaults to +1 (US) if not specified.  

Formatting is flexible, however for the most predictable results use the E.164 format.

#### Formatting Examples
- **Expected/Ideal Format**:
  - "+12223334444"
  - "+91223334444"
  - "+61223334444"
  
- **Valid, but not recommended**:
  - "2223334444"
  - "+1 (222) 333-4444"
  - "+1 222 333 4444"
  - "222-333-4444"

- **Invalid**:
  - "12223334444"
  - "552223334444"
  - "non-numeric characters"
  - "2223334444 ext. 123"

#### task
- **Type**: string  
- **Required**: Yes  
- **Description**: Provide instructions, relevant information, and examples of the ideal conversation flow.

---

### Best Practices

#### Out-of-the-Box Behaviors (Summarized):
- Speech pattern: Direct, concise, casual
- Spells out symbols, acronyms, abbreviations, percentages, etc.  
  Ex: "$4,000,000" -> “four million dollars”
- Asks clarifying questions
- Ends call when objective is complete or voicemail is detected

#### Prompting Tips:
- Want to easily test out exactly how your agent will behave?  
  Try out **Agent Testing**!
- Aim for less than >2,000 characters where possible.
- Simple, direct prompts are the most predictable and reliable.
- Frame instructions positively:  
  "Do this" rather than "Don't do this".  
  Ex: “Keep the conversation casual” rather than “Don’t be too formal”.  
  This gives concrete examples of what to do, instead of leaving expected behavior open to interpretation.

---

### Response

| Name     | Type   | Description                                       |
|----------|--------|---------------------------------------------------|
| status   | string | Can be success or error.                         |
| call_id  | string | A unique identifier for the call (present only if status is success). |

---

curl --request POST \
  --url https://api.bland.ai/v1/calls \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "phone_number": "<string>",
  "task": "<string>"
}'

import requests

url = "https://api.bland.ai/v1/calls"

payload = {
    "phone_number": "<string>",
    "task": "<string>"
}
headers = {
    "authorization": "<authorization>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

{
  "status": "success",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1"
}


## Send Call using Pathways (Simple)
Send an AI phone call with your own conversational pathway agent!  
Links - [Video Tutorial](#) | [Step-by-step web tutorial](#)

**POST**  
`/v1/calls`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name        | Type   | Required | Description                                          |
|-------------|--------|----------|------------------------------------------------------|
| phone_number| string | *        | Enter phone_number                                   |
| pathway_id  | string | *        | Enter pathway_id                                     |

---

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

---

### Body
#### phone_number
- **Type**: string  
- **Required**: Yes  
- **Description**: The phone number to call. Country code defaults to +1 (US) if not specified.  

Formatting is flexible, however for the most predictable results use the E.164 format.

#### Formatting Examples
- **Expected/Ideal Format**:
  - "+12223334444"
  - "+91223334444"
  - "+61223334444"
  
- **Valid, but not recommended**:
  - "2223334444"
  - "+1 (222) 333-4444"
  - "+1 222 333 4444"
  - "222-333-4444"

- **Invalid**:
  - "12223334444"
  - "552223334444"
  - "non-numeric characters"
  - "2223334444 ext. 123"

#### pathway_id
- **Type**: string  
- **Required**: Yes  
- **Description**: Follows the conversational pathway you created to guide the conversation.  
You can access your pathway_id by clicking on the ‘Copy ID’ button on your pathways here. If you don’t have any pathways, click the ‘Create Pathway’ button to create one!

---

### Conversational Pathway Tutorial
- [Video tutorial](#)
- [Step by step Web Tutorial](#)

---

### Response

| Name     | Type   | Description                                       |
|----------|--------|---------------------------------------------------|
| status   | string | Can be success or error.                         |
| call_id  | string | A unique identifier for the call (present only if status is success). |


curl --request POST \
  --url https://api.bland.ai/v1/calls \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "phone_number": "<string>",
  "pathway_id": "<string>"
}'

import requests

url = "https://api.bland.ai/v1/calls"

payload = {
    "phone_number": "<string>",
    "pathway_id": "<string>"
}
headers = {
    "authorization": "<authorization>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

{
  "status": "success",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1"
}


## Send Call
Send an AI phone call with a custom objective and actions.

**POST**  
`/v1/calls`  
Send

### Header
| Name           | Type   | Required | Description                                   |
|----------------|--------|----------|-----------------------------------------------|
| authorization  | string | *        | Enter authorization                           |
| encrypted_key  | string |          | Enter encrypted_key (required for BYOT)       |

### Body
| Name                 | Type   | Required | Description                                                  |
|----------------------|--------|----------|--------------------------------------------------------------|
| phone_number         | string | *        | Enter phone_number                                           |
| task                 | string | *        | Enter task                                                   |
| pathway_id           | string | *        | Enter pathway_id                                             |
| start_node_id        | string | *        | Enter start_node_id                                          |
| voice                | string | *        | Enter voice                                                  |
| background_track    | string | *        | Enter background_track                                       |
| first_sentence       | string | *        | Enter first_sentence                                         |
| wait_for_greeting    | boolean| *        | Select option                                                |
| block_interruptions  | boolean| *        | Select option                                                |
| interruption_threshold| number| *        | Enter interruption_threshold                                 |
| model                | string | *        | Enter model                                                  |
| temperature          | number | *        | Enter temperature                                            |
| keywords             | array  | *        | Enter keywords                                               |
| pronunciation_guide  | array  | *        | Enter pronunciation_guide                                     |
| transfer_phone_number| string | *        | Enter transfer_phone_number                                   |
| transfer_list        | object | *        | Enter transfer_list                                           |
| language             | string | *        | Enter language                                                |
| timezone             | string | *        | Enter timezone                                                |
| request_data         | object | *        | Enter request_data                                            |
| tools                | array  | *        | Enter tools                                                   |
| dynamic_data         | array  | *        | Enter dynamic_data                                            |
| start_time           | string | *        | Enter start_time                                              |
| voicemail_message    | string | *        | Enter voicemail_message                                       |
| voicemail_action     | object | *        | Enter voicemail_action                                        |
| retry                | object | *        | Enter retry                                                   |
| max_duration         | integer| *        | Enter max_duration                                            |
| record               | boolean| *        | Select option                                                |
| from                 | string | *        | Enter from                                                   |
| webhook              | string | *        | Enter webhook                                                |
| webhook_events       | array  | *        | Enter webhook_events                                          |
| metadata             | object | *        | Enter metadata                                                |
| summary_prompt       | string | *        | Enter summary_prompt                                          |
| analysis_prompt      | string | *        | Enter analysis_prompt                                         |
| analysis_schema      | object | *        | Enter analysis_schema                                         |
| answered_by_enabled | boolean| *        | Select option                                                |

---

### Headers

#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

#### encrypted_key
- **Type**: string  
- **Required**: No  
- **Description**: A special key for using a BYOT (Bring Your Own Twilio) account. Only required for sending calls from your own Twilio account.

---

### Body

#### phone_number
- **Type**: string  
- **Required**: Yes  
- **Description**: The phone number to call. Country code defaults to +1 (US) if not specified.

Formatting is flexible, however for the most predictable results use the E.164 format.

#### Formatting Examples
- **Expected/Ideal Format**:
  - "+12223334444"
  - "+91223334444"
  - "+61223334444"
  
- **Valid, but not recommended**:
  - "2223334444"
  - "+1 (222) 333-4444"
  - "+1 222 333 4444"
  - "222-333-4444"

- **Invalid**:
  - "12223334444"
  - "552223334444"
  - "non-numeric characters"
  - "2223334444 ext. 123"

#### task
- **Type**: string  
- **Required**: Yes  
- **Description**: Provide instructions, relevant information, and examples of the ideal conversation flow.

This is your prompt where you are telling the agent what to do.

**Recommendations**:
- Include context and a background/persona for the agent like "You are {name}, a customer service agent at {company} calling {name} about {reason}".
- Phrase instructions like you are speaking to the agent before the call.
- Any time you tell the agent not to do something, provide an example of what they should do instead.
- Keep the prompt under 2,000 characters where possible.

Want to easily test out exactly how your agent will behave? Try out **Agent Testing**!

#### pathway_id
- **Type**: string  
- **Required**: Yes  
- **Description**: This is the pathway ID for the pathway you have created on our dev portal. You can access the ID of your pathways by clicking the ‘Copy ID’ button of your pathway here.

**Note**: Certain parameters do not apply when using pathways.

##### Unused Parameters:
- **task**: The pathway substitutes as the agent’s instructions.
- **model**: We use our own fine-tuned models under the hood.
- **tools**: Replaced by ‘Webhook’ Node in Pathways.
- **transfer_list**: Replaced by ‘Transfer Call’ Node in Pathways.
- **transfer_phone_number**: Replaced by ‘Transfer Call’ Node in Pathways.

##### Example Simple Request body:
```json
{
  "phone_number": "+1975934749",
  "pathway_id": "a0f0d4ed-f5f5-4f16-b3f9-22166594d7a7"
}


start_node_id
Type: string
Required: Yes
Description: This is the node ID for the node you want the pathway to start from. You can access the ID of your nodes here.
Note: This parameter is only used when pathway_id is provided.

Example Simple Request body:
json
Copy code
{
  "phone_number": "+1975934749",
  "pathway_id": "a0f0d4ed-f5f5-4f16-b3f9-22166594d7a7",
  "start_node_id": "a0cd5fed-f3f3-5412-1339-13567921d7b8"
}
Agent Parameters (Body)
voice
Type: string
Default: "mason"
Description: The voice of the AI agent to use. Accepts any form of voice ID, including custom voice clones and voice presets.
Example: "voice": "maya"

Bland Curated voices:

maya
mason
ryan
adriana
tina
matt
evelyn
background_track
Type: string
Description: Select an audio track that you’d like to play in the background during the call.
Options:

null: Default, will play audible but quiet phone static.
office: Office-style soundscape. Includes faint typing, chatter, clicks, and other office sounds.
cafe: Cafe-like soundscape. Includes faint talking, clinking, and other cafe sounds.
restaurant: Similar to cafe, but more subtle.
none: Minimizes background noise.
first_sentence
Type: string
Description: Makes your agent say a specific phrase or sentence for its first response.
wait_for_greeting
Type: boolean
Default: false
Description: When set to true, the agent will wait for the call recipient to speak first before responding.
block_interruptions
Type: boolean
Default: false
Description: When set to true, the AI will not respond or process interruptions from the user.
interruption_threshold
Type: number
Default: 100
Description: Adjusts how patient the AI is when waiting for the user to finish speaking.
Recommended range: 50-200

model
Type: string
Default: "enhanced"
Description: Select a model to use for your call.
Options:

base
turbo
enhanced
temperature
Type: float
Default: "0.7"
Description: Controls the randomness of the LLM.
Example Values: "0.9", "0.3", "0.5"

keywords
Type: string[]
Default: "[]"
Description: Words to be boosted in the transcription engine.
pronunciation_guide
Type: array
Description: Guide the agent on how to pronounce specific words.
Example:

json
Copy code
[
  {
    "word": "example",
    "pronunciation": "ex-am-ple",
    "case_sensitive": "false",
    "spaced": "false"
  },
  {
    "word": "API",
    "pronunciation": "A P I",
    "case_sensitive": "true",
    "spaced": "true"
  }
]
transfer_phone_number
Type: string
Description: A phone number that the agent can transfer to under specific conditions.
transfer_list
Type: object
Description: Provides multiple phone numbers to transfer calls to based on context.
Example:

json
Copy code
{
  "transfer_list": {
    "default": "+12223334444",
    "sales": "+12223334444",
    "support": "+12223334444",
    "billing": "+12223334444"
  }
}
language
Type: string
Default: "en-US"
Description: Select a supported language of your choice.
Available language options:

en-US, en-GB, en-AU, en-NZ, en-IN, etc.
timezone
Type: string
Default: "America/Los_Angeles"
Description: Set the timezone for the call.
Response
Name	Type	Description
status	string	Can be success or error.
call_id	string	A unique identifier for the call (present only if status is success).
batch_id	string	The batch ID of the call (present only if status is success).
message	string	A message explaining the status of the call.
errors	array	A detailed list of each field with an error and its error message.
Example of error:

json
Copy code
{
  "status": "error",
  "message": "Invalid parameters",
  "errors": [
    "Missing required parameter: phone_number.",
    "Missing required parameter: task.",
    "Phone number must be a string or number.",
    "Task must be a string."
  ]
}

curl --request POST \
  --url https://api.bland.ai/v1/calls \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "phone_number": "<string>",
  "task": "<string>",
  "pathway_id": "<string>",
  "start_node_id": "<string>",
  "voice": "<string>",
  "background_track": "<string>",
  "first_sentence": "<string>",
  "wait_for_greeting": true,
  "block_interruptions": true,
  "interruption_threshold": 123,
  "model": "<string>",
  "temperature": 123,
  "keywords": [
    "<string>"
  ],
  "pronunciation_guide": [
    {}
  ],
  "transfer_phone_number": "<string>",
  "transfer_list": {},
  "language": "<string>",
  "timezone": "<string>",
  "request_data": {},
  "tools": [
    {}
  ],
  "dynamic_data": [
    {
      "dynamic_data[i].response_data": [
        {}
      ]
    }
  ],
  "start_time": "<string>",
  "voicemail_message": "<string>",
  "voicemail_action": {},
  "retry": {},
  "max_duration": 123,
  "record": true,
  "from": "<string>",
  "webhook": "<string>",
  "webhook_events": [
    "<string>"
  ],
  "metadata": {},
  "summary_prompt": "<string>",
  "analysis_prompt": "<string>",
  "analysis_schema": {},
  "answered_by_enabled": true
}'

import requests

url = "https://api.bland.ai/v1/calls"

payload = {
    "phone_number": "<string>",
    "task": "<string>",
    "pathway_id": "<string>",
    "start_node_id": "<string>",
    "voice": "<string>",
    "background_track": "<string>",
    "first_sentence": "<string>",
    "wait_for_greeting": True,
    "block_interruptions": True,
    "interruption_threshold": 123,
    "model": "<string>",
    "temperature": 123,
    "keywords": ["<string>"],
    "pronunciation_guide": [{}],
    "transfer_phone_number": "<string>",
    "transfer_list": {},
    "language": "<string>",
    "timezone": "<string>",
    "request_data": {},
    "tools": [{}],
    "dynamic_data": [{"dynamic_data[i].response_data": [{}]}],
    "start_time": "<string>",
    "voicemail_message": "<string>",
    "voicemail_action": {},
    "retry": {},
    "max_duration": 123,
    "record": True,
    "from": "<string>",
    "webhook": "<string>",
    "webhook_events": ["<string>"],
    "metadata": {},
    "summary_prompt": "<string>",
    "analysis_prompt": "<string>",
    "analysis_schema": {},
    "answered_by_enabled": True
}
headers = {
    "authorization": "<authorization>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

const options = {
  method: 'POST',
  headers: {authorization: '<authorization>', 'Content-Type': 'application/json'},
  body: '{"phone_number":"<string>","task":"<string>","pathway_id":"<string>","start_node_id":"<string>","voice":"<string>","background_track":"<string>","first_sentence":"<string>","wait_for_greeting":true,"block_interruptions":true,"interruption_threshold":123,"model":"<string>","temperature":123,"keywords":["<string>"],"pronunciation_guide":[{}],"transfer_phone_number":"<string>","transfer_list":{},"language":"<string>","timezone":"<string>","request_data":{},"tools":[{}],"dynamic_data":[{"dynamic_data[i].response_data":[{}]}],"start_time":"<string>","voicemail_message":"<string>","voicemail_action":{},"retry":{},"max_duration":123,"record":true,"from":"<string>","webhook":"<string>","webhook_events":["<string>"],"metadata":{},"summary_prompt":"<string>","analysis_prompt":"<string>","analysis_schema":{},"answered_by_enabled":true}'
};

fetch('https://api.bland.ai/v1/calls', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

  {
  "status": "success",
  "message": "Call successfully queued.",
  "call_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
  "batch_id": null
}


## Calls
### Analyze Call with AI
Analyzes a call of calls based using questions and goals.

**POST**  
`/v1/calls/{call_id}/analyze`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name     | Type   | Required | Description                          |
|----------|--------|----------|--------------------------------------|
| call_id  | string | *        | Enter call_id                        |

### Body
| Name      | Type   | Required | Description                                          |
|-----------|--------|----------|------------------------------------------------------|
| goal      | string | *        | Enter goal                                           |
| questions  | array  | *        | An array of questions to be analyzed for the call.  |

#### Headers
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | required | Your API key for authentication.    |

#### Path Parameters
| Name     | Type   | Required | Description                          |
|----------|--------|----------|--------------------------------------|
| call_id  | string | required | The unique identifier for the call to be analyzed. |

#### Request Body
| Name      | Type   | Required | Description                                          |
|-----------|--------|----------|------------------------------------------------------|
| goal      | string | required | This is the overall purpose of the call. Provides context for the analysis to guide how the questions/transcripts are interpreted. |
| questions  | array  | required | An array of questions to be analyzed for the call. Each question should be an array with two elements: the question text and the expected answer type (e.g., “string”, “boolean”). Fairly flexible in terms of the expected answer type, and unanswerable questions will default to null. |

#### Examples
"questions": [
      ["Who answered the call?", "human or voicemail"],
      ["Positive feedback about the product: ", "string"],
      ["Negative feedback about the product: ", "string"],
      ["Customer confirmed they were satisfied", "boolean"]
  ],

Response

status
object
Will be success if the request was successful.

message
string
Confirms the request was successful, or provides an error message if the request failed.

answers
array
Contains the analyzed answers for the call in an array.

credits_used
number
Token-based price for the analysis request.

As a rough estimate, the base cost is 0.003 credits with an additional 0.0015 credits per call in the call.

Longer call transcripts and higher numbers of questions can increase the cost, however the cost scales very effectively with calls vs. individual calls.

curl --request POST \
  --url https://api.bland.ai/v1/calls/{call_id}/analyze \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "goal": "<string>",
  "questions": [
    [
      "<string>"
    ]
  ]
}'

import requests

url = "https://api.bland.ai/v1/calls/{call_id}/analyze"

payload = {
    "goal": "<string>",
    "questions": [["<string>"]]
}
headers = {
    "authorization": "<authorization>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

const options = {
  method: 'POST',
  headers: {authorization: '<authorization>', 'Content-Type': 'application/json'},
  body: '{"goal":"<string>","questions":[["<string>"]]}'
};

fetch('https://api.bland.ai/v1/calls/{call_id}/analyze', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

  {
    "status": "success",
    "message": "Successfully analyzed call",
    "answers": [
        "human",
        "Customer found the product sturdy and reliable",
        "A bit heavy",
        true
    ]
}


## Stop Active Call
End an active phone call by call_id.

**POST**  
`/v1/calls/{call_id}/stop`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name     | Type   | Required | Description                          |
|----------|--------|----------|--------------------------------------|
| call_id  | string | *        | Enter call_id                        |

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

### Path Parameters
#### call_id
- **Type**: string  
- **Required**: Yes  
- **Description**: The unique identifier for the call you want to end.

### Response
| Name     | Type   | Description                                       |
|----------|--------|---------------------------------------------------|
| status   | string | Can be success or error.                         |
| message  | string | If the status is success, the message will say “Call ended successfully.” Otherwise, if the status is error, the message will say “SID not found for the given c_id.” or “Internal server error.”



curl --request POST \
  --url https://api.bland.ai/v1/calls/{call_id}/stop \
  --header 'authorization: <authorization>'

  import requests

url = "https://api.bland.ai/v1/calls/{call_id}/stop"

headers = {"authorization": "<authorization>"}

response = requests.request("POST", url, headers=headers)

print(response.text)

const options = {method: 'POST', headers: {authorization: '<authorization>'}};

fetch('https://api.bland.ai/v1/calls/{call_id}/stop', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

  {
  "status": "success",
  "message": "Call ended successfully."
}


## Stop All Active Calls
End all active phone calls on your account.

**POST**  
`/v1/calls/active/stop`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | Can be success or error.                         |
| message   | string   | If the status is success, the message will say “Call ended successfully.” Otherwise, if the status is error, the message will say “SID not found for the given c_id.” or “Internal server error.” |
| num_calls | integer  | The number of active calls that will be cancelled. |


curl --request POST \
  --url https://us.api.bland.ai/v1/calls/active/stop \
  --header 'authorization: <authorization>'


PYTHON
import requests

url = "https://us.api.bland.ai/v1/calls/active/stop"

headers = {"authorization": "<authorization>"}

response = requests.request("POST", url, headers=headers)

print(response.text)

JAVASCRIPT

const options = {method: 'POST', headers: {authorization: '<authorization>'}};

fetch('https://us.api.bland.ai/v1/calls/active/stop', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

  __
response

  {
  "status": "success",
  "message": "Stopping active calls. This may take some time...",
  "num_calls": 12
}



### GET
`/v1/calls`
Send

### Header
| Name           | Type   | Required | Description                                   |
|----------------|--------|----------|-----------------------------------------------|
| authorization  | string | *        | Enter authorization                           |
| encrypted_key  | string |          | Use your own Twilio account and only return inbound numbers associated with that account sid (optional). |

### Query
| Name           | Type     | Description                                                                 |
|----------------|----------|-----------------------------------------------------------------------------|
| from_number    | string   | Filter calls by the number they were dispatched from.                      |
| to_number      | string   | Filter calls by the number they were dispatched to.                        |
| from           | integer  | The starting index (inclusive) for the range of calls to retrieve.        |
| to             | integer  | The ending index for the range of calls to retrieve.                      |
| limit          | integer  | The maximum number of calls to return in the response. Default: "1000"    |
| ascending      | boolean  | Whether to sort the calls in ascending order of their creation time. Default: "false" |
| start_date     | string   | Get calls including and after a specific date. Format: YYYY-MM-DD        |
| end_date       | string   | Get calls including and before a specific date. Format: YYYY-MM-DD        |
| created_at     | string   | Get calls for a specific date. Can’t be used with end_date or start_date. Format: YYYY-MM-DD |
| completed      | boolean  | Whether to filter calls by complete status.                                |
| batch_id       | string   | Get calls from a specific batch.                                          |
| answered_by    | string   | Filter by answered_by type. Example: human                                |
| inbound        | boolean  | Whether to filter based on inbound or not.                                |
| duration_gt    | number   | Duration (Call Length) greater than the value provided. Example: 0.5 (This would be equal to half a minute) |
| duration_lt    | number   | Duration (Call Length) less than the value provided. Example: 0.5 (This would be equal to half a minute) |
| campaign_id    | string   | Get calls for a specific campaign id.                                     |

### Response
| Name         | Type     | Description                                                                 |
|--------------|----------|-----------------------------------------------------------------------------|
| total_count  | integer  | The total number of calls that match the query filters.                    |
| count        | integer  | The number of calls returned in the response.                              |
| calls        | array    | An array of call data objects. See the Call section for details.          |
|              |          | Note: Individual call transcripts are not included due to their size.     |


CURL

curl --request GET \
  --url https://api.bland.ai/v1/calls \
  --header 'authorization: <authorization>'

PYTHON

import requests

url = "https://api.bland.ai/v1/calls"

headers = {"authorization": "<authorization>"}

response = requests.request("GET", url, headers=headers)

print(response.text)

JAVASCRIPT

const options = {method: 'GET', headers: {authorization: '<authorization>'}};

fetch('https://api.bland.ai/v1/calls', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

  RESPONSE

  {
    "count": 784,
    "calls": [
        {
            "call_id": "c1234567-89ab-cdef-0123-456789abcdef",
            "created_at": "2023-12-21T23:25:14.801193+00:00",
            "call_length": 0.834, // minutes
            "to": "5551234567",
            "from": "+15551234567",
            "completed": true,
            "queue_status": "complete",
            "error_message": null,
            "answered_by": "human",
            "batch_id": "b1234567-89ab-cdef-0123-gen-batch",
        },
        //... Additional call objects
    ]
}



### Call Details
Retrieve detailed information, metadata and transcripts for a call.

**GET**  
`/v1/calls/{call_id}`  
Send

#### Header
| Name           | Type   | Required | Description                                   |
|----------------|--------|----------|-----------------------------------------------|
| authorization  | string | *        | Enter authorization                           |
| encrypted_key  | string |          | Enter encrypted_key                           |

#### Path
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | *        | Enter call_id                                 |

#### Headers
| Name           | Type   | Required | Description                                   |
|----------------|--------|----------|-----------------------------------------------|
| authorization  | string | required | Your API key for authentication.              |
| encrypted_key  | string | optional | Use your own Twilio account and only return inbound numbers associated with that account sid. |

#### Path Parameters
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | required | The unique identifier of the call for which you want to retrieve detailed information. |

#### Response
| Name                | Type                | Description                                                                 |
|---------------------|---------------------|-----------------------------------------------------------------------------|
| transcripts         | array of objects    | An array of phrases spoken during the call. Each index includes:            |
|                     |                     | - **id**: Unique identifier for the transcript.                             |
|                     |                     | - **created_at**: Timestamp of when the phrase was spoken.                 |
|                     |                     | - **text**: The text of the spoken phrase.                                  |
|                     |                     | - **user**: Can be user, assistant, robot, or agent-action.                |
| call_id             | number              | The unique identifier for the call.                                        |
| call_length         | number              | The length of the call in minutes.                                         |
| transferred_to      | string              | Number that the person was transferred to.                                 |
| batch_id            | string              | If the call is part of a batch, its batch_id will be here.                |
| to                  | string              | The phone number that received the call.                                   |
| from                | string              | The phone number that made the call.                                       |
| request_data        | object              | Details about parameters in the original API request.                      |
| completed           | boolean             | Whether the call has been completed.                                       |
| inbound             | boolean             | Whether the call was inbound or outbound. Will be false for outbound calls.|
| created_at          | string              | The timestamp for when the call request was created.                      |
| started_at          | string              | The time the call was connected.                                          |
| end_at              | string              | The time that the call will automatically be ended at if it’s still connected (because of max_duration). |
| queue_status        | string              | The status of the call. During extremely high volume periods, calls may be queued for a short period of time before being dispatched. |

**Statuses:**
- **new**: An API request has been received.
- **queued**: Call parameters have been validated and authentication succeeded.
- **allocated**: Extremely brief, the call is being dispatched.
- **started**: The phone call is live and in progress.
- **complete**: The phone call has ended successfully.
- **pre_queue_error**: An error occurred before the call was queued. Invalid parameters generally cause this.
- **queue_error**: Error occurred while the call was queued. Ex. Valid phone number but to an unserviced area.
- **call_error**: Error occurred during live call. May be caused by transferring to an invalid phone number or an unforeseen error.
- **complete_error**: Error occurred after the call was completed. Ex. A post-call webhook failed.

If at any point an error occurs, it will be recorded in the error_message field.

| Name                | Type                | Description                                                                 |
|---------------------|---------------------|-----------------------------------------------------------------------------|
| endpoint_url        | string              | The URL of the deployment that the call was handled on. Will always be “api.prod.bland.ai” unless the call was handled on a custom Enterprise deployment. |
| max_duration         | number              | The maximum length of time the call was allowed to last. If the call would exceed this length, it’s ended early. |
| error_message       | string              | If an error occurs, this will contain a description of the error. Otherwise, it will be null. |
| variables           | object              | Variables created during the call - both system variables as well as generated with dynamic_data or Custom Tools. |
| answered_by         | string              | If answered_by_enabled was set to true in the original API request, this field contains one of the following values: |
|                     |                     | - **human**: The call was answered by a human.                             |
|                     |                     | - **voicemail**: The call was answered by an answering machine or voicemail.|
|                     |                     | - **unknown**: There was not enough audio at the start of the call to make a determination. |
|                     |                     | - **no-answer**: The call was not answered.                                 |
|                     |                     | - **null**: Not enabled, or still processing the result.                    |
| Notes:             |                     |                                                                             |
| record              | boolean             | Whether the call audio was recorded.                                       |
| recording_url       | string              | The URL of the recording of the call. Only available if record was set to true in the original API request. |
| metadata            | object              | Metadata about the call. This can include information about the client, customer, or any other data you want to include. This is identical to the metadata that was set in the original API request to send the call. |
| summary             | string              | A short summary of the call based off of the transcript that’s generated when the call ends. |
| price               | number              | The cost of the call in USD.                                              |
| local_dialing      | boolean             | Whether Local Dialing was enabled for your account at the time of the call. |
| call_ended_by      | string              | Whether the call was ended by Bland’s system or the other end of the line. |
|                     |                     | - **ASSISTANT**: The agent ended the call.                                 |
|                     |                     | - **USER**: The user ended the call.                                      |
| pathway_logs        | string              | Pathways calls will have extra logs here that have much more detailed information about the chosen nodes and internal reasoning throughout the flow. |
| analysis_schema     | object              | The provided structure used in the post call analysis. This is the raw skeleton describing the data structure that will be filled in once the call ends. |
| analysis            | object              | The data filled in by the post call analysis. This is the raw data that was generated by the analysis schema. |
| concatenated_transcript | string          | A single string containing all of the text from the call. Excludes system messages and auto-generated data. |
| transcripts         | array of objects    | An array of phrases spoken during the call. Each index includes:            |
|                     |                     | - **id**: Unique identifier for the transcript.                             |
|                     |                     | - **created_at**: Timestamp of when the phrase was spoken.                 |
|                     |                     | - **text**: The text of the spoken phrase.                                  |
|                     |                     | - **user**: Can be user, assistant, robot, or agent-action.                |
| status              | string              | The status of the call. This is the most up-to-date status of the call, but is only present for calls that have been successfully created. |
| corrected_duration  | string              | The corrected duration of the call in seconds. This is the actual length of the call, not the max_duration. 



CURL
curl --request GET \
  --url https://api.bland.ai/v1/calls/{call_id} \
  --header 'authorization: <authorization>'

PYTHON

import requests

url = "https://api.bland.ai/v1/calls/{call_id}"

headers = {"authorization": "<authorization>"}

response = requests.request("GET", url, headers=headers)

print(response.text)

JAVASCRIPT
const options = {method: 'GET', headers: {authorization: '<authorization>'}};

fetch('https://api.bland.ai/v1/calls/{call_id}', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

RESPONSE


{
    "call_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
    "call_length": 0.75,
    "batch_id": null,
    "to": "+12223334444",
    "from": "+17163511654",
    "request_data": {
        "phone_number": "+12223334444",
        "wait": true,
        "language": "ENG"
    },
    "completed": true,
    "created_at": "2024-04-27T23:51:18.025251+00:00",
    "inbound": false,
    "queue_status": "completed",
    "endpoint_url": "api.prod.bland.ai",
    "max_duration": 30,
    "error_message": null,
    "variables": {
        "now": "Sat Apr 27 2024 18:51:25 GMT-0500 (Central Daylight Time)",
        "now_utc": "Sat, 27 Apr 2024 23:51:25 GMT",
        "short_from": "7163511654",
        "short_to": "2223334444",
        "from": "+17163511654",
        "to": "+12223334444",
        "call_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
        "phone_number": "+12223334444",
        "city": "SAN FRANCISCO",
        "country": "US",
        "state": "CA",
        "zip": "12345",
        "input": {
            "date": "2024-04-28",
            "rooms": 3
        }
    },
    "answered_by": "human",
    "record": false,
    "recording_url": null,
    "c_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
    "metadata": {},
    "summary": "The call was a conversation between a hotel booking service assistant and a customer. The customer expressed interest in booking a hotel room for tomorrow and needing three rooms. The assistant booked book the reservation for three rooms for the next day. Then, the call ended with the assistant thanking the customer for choosing their service.",
    "price": 0.068,
    "started_at": "2024-04-27T23:51:25+00:00",
    "local_dialing": false,
    "call_ended_by": "ASSISTANT",
    "pathway_logs": null,
    "analysis_schema": null,
    "analysis": null,
    "concatenated_transcript": "user: Hello? \n assistant: Hi there! I'm calling from the hotel booking service. I'd love to help you with your reservation. Could you let me know what day you'd like to book your hotel for and how many rooms you'll need? \n user: Hopefully, tomorrow, I'm thinking. ...",
    "transcripts": [
        {
            "id": 7395694,
            "created_at": "2024-04-27T23:51:28.568385+00:00",
            "text": "Hello?",
            "user": "user",
            "c_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
            "status": null,
            "transcript_id": null
        },
        {
            "id": 7395698,
            "created_at": "2024-04-27T23:51:30.689815+00:00",
            "text": "Hi there! I'm calling from the hotel booking service. I'd love to help you with your reservation. Could you let me know what day you'd like to book your hotel for and how many rooms you'll need?",
            "user": "assistant",
            "c_id": "d9cce3f3-23cf-4fa7-b62c-8be8119b8715",
            "status": null,
            "transcript_id": "c58ee235-0763-4ae1-a734-17fbba505c52"
        },
        //...
    ],
    "status": "completed",
    "corrected_duration": "45",
    "end_at": "2024-04-27T23:52:10.000Z"
}


## Calls
### Event Stream
Retrieve stream of events that occurred during the call.

**GET**  
`/v1/event_stream/{call_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | *        | Enter call_id                                 |

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

### Path Parameters
#### call_id
- **Type**: string  
- **Required**: Yes  
- **Description**: The unique identifier of the call for which you want to retrieve detailed information.

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| level     | string   | The level of the event - queue or call           |
| message   | string   | The message of the event.                         |
| category  | string   | The category of the event - info, performance or error. |
| call_id   | string   | The unique identifier for the call.              |
| timestamp | string   | When the event occurred.                          |

### cURL
curl --request GET \
  --url https://api.bland.ai/v1/event_stream/{call_id} \
  --header 'authorization: <authorization>'

RESPONSE
  {
  "level": "<string>",
  "message": "<string>",
  "category": "<string>",
  "call_id": "<string>",
  "timestamp": "<string>"
}




## Calls
### Audio Recording
Retrieve your call’s audio recording.

**GET**  
`/v1/calls/{call_id}/recording`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |
| accept        | string | *        | Enter accept                         |

### Path
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | *        | Enter call_id                                 |

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

#### accept
- **Type**: string  
- **Required**: Yes  
- **Description**: Must be application/json to receive a url, or audio/mpeg to receive the audio file.

### Path Parameters
#### call_id
- **Type**: string  
- **Required**: Yes  
- **Description**: The ID of the call to retrieve the recording for.

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | Can be success or error.                         |
| message   | string   | If the status is success, the url field will be present. A 404 error will be returned if the call does not exist or the recording is not available. We can only retrieve recordings if the call was created with record set to true. A 400/500 error will be returned if there is an error retrieving the recording. |
| url       | string   | If the status is success, the url will provide the exact location of the MP3 file storing the call’s audio. |

### cURL
curl --request GET \
  --url https://api.bland.ai/v1/calls/{call_id}/recording

RESPONSE - SUCCESS

{
  "status": "success",
  "url": "https://URL-TO-FILE.mp3"
}


Success Response 'audio/mpeg'
(returns the audio file)


ERROR RESPONSE
{
  "status": "error",
  "message": "Error fetching recording"
}


### Calls
Get corrected transcripts
Analyzes a call of calls based using questions and goals.

**GET**  
`/v1/calls/{call_id}/correct`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | *        | Enter call_id                                 |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Path Parameters
| Name     | Type   | Required | Description                                   |
|----------|--------|----------|-----------------------------------------------|
| call_id  | string | required | The unique identifier for the call to be corrected. |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | object   | Will be success if the request was successful.   |
| message   | string   | Confirms the request was successful, or provides an error message if the request failed. |
| corrected | array    | This will contain an array of objects. Each object will be constructed as the following: |

CURL 
curl --request GET \
  --url https://api.bland.ai/v1/calls/{call_id}/correct \
  --header 'authorization: <authorization>'

RESPONSE
{
    "corrected": [
        {
            "start": 0.069,
            "end": 2.551,
            "text": " Hi, I'm calling about a pizza order.",
            "speaker": 0
        },
        {
            "start": 2.551,
            "end": 4.932,
            "text": "Could I get your name, please?",
            "speaker": 0
        },
        {
            "start": 4.932,
            "end": 8.074,
            "text": "Yeah, my name is John.",
            "speaker": 1
        },
        {
            "start": 8.074,
            "end": 8.875,
            "text": "Great.",
            "speaker": 0
        },
        {
            "start": 8.875,
            "end": 9.876,
            "text": "Thanks, John.",
            "speaker": 0
        },
        {
            "start": 9.876,
            "end": 13.038,
            "text": "Could you tell me about the pizza order you placed?",
            "speaker": 0
        },
        {
            "start": 13.038,
            "end": 16.36,
            "text": "Yeah, I want a pepperoni.",
            "speaker": 2
        },
        {
            "start": 16.36,
            "end": 17.1,
            "text": "Oh, okay.",
            "speaker": 0
        },
        {
            "start": 17.1,
            "end": 18.521,
            "text": "One pepperoni pizza.",
            "speaker": 0
        },
        {
            "start": 18.521,
            "end": 19.682,
            "text": "Anything else with that order?",
            "speaker": 0
        },
        {
            "start": 19.682,
            "end": 23.665,
            "text": "No, actually, can we cancel it?",
            "speaker": 1
        },
        {
            "start": 23.665,
            "end": 26.306,
            "text": "I gotta go.",
            "speaker": 1
        },
        {
            "start": 26.306,
            "end": 27.427,
            "text": "No problem.",
            "speaker": 0
        },
        {
            "start": 27.427,
            "end": 28.668,
            "text": "I'll cancel the order for you.",
            "speaker": 0
        },
        {
            "start": 29.144,
            "end": 30.587,
            "text": " Thanks for letting me know.",
            "speaker": 0
        },
        {
            "start": 30.587,
            "end": 31.189,
            "text": "Have a good one.",
            "speaker": 0
        }
    ],
    "status": "success",
    "aligned": [
        {
            "start": 0.069,
            "end": 2.551,
            "text": " Hi, I'm calling about a pizza order.",
            "speaker": "assistant",
            "similarity": 0.686406472983644
        },
        {
            "start": 2.551,
            "end": 4.932,
            "text": "Could I get your name, please?",
            "speaker": "assistant",
            "similarity": 0.6793662204867575
        },
        {
            "start": 4.932,
            "end": 8.074,
            "text": "Yeah, my name is John.",
            "speaker": "user",
            "similarity": 0.9999999999999998
        },
        {
            "start": 8.074,
            "end": 8.875,
            "text": "Great.",
            "speaker": "assistant",
            "similarity": 0.2581988897471611
        },
        {
            "start": 8.875,
            "end": 9.876,
            "text": "Thanks, John.",
            "speaker": "assistant",
            "similarity": 0.36514837167011066
        },
        {
            "start": 9.876,
            "end": 13.038,
            "text": "Could you tell me about the pizza order you placed?",
            "speaker": "assistant",
            "similarity": 0.894427190999916
        },
        {
            "start": 13.038,
            "end": 16.36,
            "text": "Yeah, I want a pepperoni.",
            "speaker": "user",
            "similarity": 0.7999999999999998
        },
        {
            "start": 16.36,
            "end": 17.1,
            "text": "Oh, okay.",
            "speaker": "user",
            "similarity": 0.4999999999999999
        },
        {
            "start": 17.1,
            "end": 18.521,
            "text": "One pepperoni pizza.",
            "speaker": "assistant",
            "similarity": 0.5773502691896257
        },
        {
            "start": 18.521,
            "end": 19.682,
            "text": "Anything else with that order?",
            "speaker": "assistant",
            "similarity": 0.7453559924999299
        },
        {
            "start": 19.682,
            "end": 23.665,
            "text": "No, actually, can we cancel it?",
            "speaker": "user",
            "similarity": 0.8164965809277261
        },
        {
            "start": 23.665,
            "end": 26.306,
            "text": "I gotta go.",
            "speaker": "user",
            "similarity": 0.5773502691896257
        },
        {
            "start": 26.306,
            "end": 27.427,
            "text": "No problem.",
            "speaker": "assistant",
            "similarity": 0.32444284226152503
        },
        {
            "start": 27.427,
            "end": 28.668,
            "text": "I'll cancel the order for you.",
            "speaker": "assistant",
            "similarity": 0.5202659817144719
        },
        {
            "start": 29.144,
            "end": 30.587,
            "text": " Thanks for letting me know.",
            "speaker": "assistant",
            "similarity": 0.6155870112510924
        },
        {
            "start": 30.587,
            "end": 31.189,
            "text": "Have a good one.",
            "speaker": "agent-action",
            "similarity": 0.5
        }
    ],
    "original": [
        {
            "id": 3056032,
            "created_at": "2024-02-29T18:40:49.592012+00:00",
            "text": "Okay, One pepperoni pizza. Anything else with that order?",
            "user": "assistant",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056054,
            "created_at": "2024-02-29T18:40:59.641211+00:00",
            "text": "No problem, Ill cancel the order for you. Thanks for letting me know, Have a good one!",
            "user": "assistant",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3055999,
            "created_at": "2024-02-29T18:40:40.39336+00:00",
            "text": "Yeah. My name is John. ",
            "user": "user",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056064,
            "created_at": "2024-02-29T18:41:08.152963+00:00",
            "text": "Okay. Bye. ",
            "user": "user",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3055975,
            "created_at": "2024-02-29T18:40:33.362607+00:00",
            "text": "Hi, Im calling about a pizza order. Could I get your name please?",
            "user": "assistant",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056028,
            "created_at": "2024-02-29T18:40:48.597915+00:00",
            "text": "Yeah. I want the pepperoni. ",
            "user": "user",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056066,
            "created_at": "2024-02-29T18:41:09.563502+00:00",
            "text": "Ended call: Thanks, you too! Have a good day.",
            "user": "agent-action",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056004,
            "created_at": "2024-02-29T18:40:41.26799+00:00",
            "text": "Great, Thanks John. Could you tell me about the pizza order you placed?",
            "user": "assistant",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        },
        {
            "id": 3056053,
            "created_at": "2024-02-29T18:40:58.62518+00:00",
            "text": "No. Actually, can we cancel it? I gotta go. ",
            "user": "user",
            "c_id": "bfaf99a1-b7c0-4f96-9630-90bc41cea488"
        }
    ]
}


## Knowledge Bases

### Create a Vector Store
Create a new vector store.

**POST**  
`/vectors`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name        | Type   | Required | Description                          |
|-------------|--------|----------|--------------------------------------|
| name        | string | *        | Enter name                           |
| description | string | *        | Enter description                    |
| text        | string | *        | Enter text                           |

### Usage
Pass the `vector_id` into your agent’s tools to enable the agent to use the vector store.

CURL 
curl --request POST \
  --url https://kb.bland.ai/vectors \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>",
  "text": "<string>"
}'

RESPONSE:
{
  "vector_id": "KB-55e64dae-1585-4632-ae97-c909c288c6bc"
}


## Knowledge Bases

### Update Vector Store
Update an existing vector store.

**POST**  
`/vectors/{vector_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name        | Type   | Required | Description                          |
|-------------|--------|----------|--------------------------------------|
| vector_id   | string | *        | Enter vector_id                      |

### Body
| Name        | Type     | Required | Description                          |
|-------------|----------|----------|--------------------------------------|
| name        | string   | *        | Enter name                           |
| description | string   | *        | Enter description                    |
| text        | string   | *        | Enter text                           |

### Usage
Pass the `vector_id` into your agent’s tools to enable the agent to use the vector store.


curl --request POST \
  --url https://kb.bland.ai/vectors/{vector_id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>",
  "text": "<string>"
}'

RESPONSE
{
  "vector_id": "KB-55e64dae-1585-4632-ae97-c909c288c6bc"
}


## Knowledge Bases
### List Vector Stores
List all vector stores in your account.

**GET**  
`/vectors`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Query
| Name         | Type     | Default | Description                          |
|--------------|----------|---------|--------------------------------------|
| include_text | boolean  | false   | Include the full text of the documents stored in the vector store. This can be useful for debugging, but may return large amounts of data. |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| vectors   | array    | An array of objects, for each vector store in your account. |
| vectors[].vector_id | string | The unique identifier for the vector store. |
| vectors[].name      | string | The name of the vector store.                   |
| vectors[].description | string | A description of the vector store.            |

curl --request GET \
  --url https://kb.bland.ai/vectors \
  --header 'authorization: <authorization>' \
  --data '{
  "include_text": false
}'


curl --request GET \
  --url https://kb.bland.ai/vectors \
  --header 'authorization: <authorization>'

  {
    "vectors": [
        {
            "vector_id": "KB-55e64dae-1585-4632-bc97-c909c288c6bc",
            "name": "Bland AI FAQs",
            "description": "Business facts, policies, and frequently asked questions for Bland AI."
        }
    ]
}


## Knowledge Bases
### List Vector Details
View the details for a specific vector store.

**GET**  
`/vectors/{vector_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name       | Type   | Required | Description                                   |
|------------|--------|----------|-----------------------------------------------|
| vector_id  | string | *        | Enter vector_id                               |

### Query
| Name         | Type     | Default | Description                          |
|--------------|----------|---------|--------------------------------------|
| include_text | boolean  | false   | Include the full text of the documents stored in the vector store. This can be useful for debugging, but may return large amounts of data. |

### Response
| Name        | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| vector_id   | string   | The unique identifier for the vector store.       |
| name        | string   | The name of the vector store.                      |
| description | string   | A description of the vector store.                |



curl --request GET \
  --url https://kb.bland.ai/vectors/{vector_id} \
  --header 'authorization: <authorization>'

RESPONSE

{
    {
        "vector_id": "KB-55e64dae-1585-4632-ae97-c909c288c6bc",
        "name": "Bland AI FAQs",
        "description": "Business facts, policies, and frequently asked questions for Bland AI."
    }
}


## Knowledge Bases
### Delete Vector Store
Remove a vector store from your account.

**POST**  
`/vectors/{vector_id}/delete`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name       | Type   | Required | Description                                   |
|------------|--------|----------|-----------------------------------------------|
| vector_id  | string | *        | Enter vector_id                               |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name       | Type     | Required | Description                                   |
|------------|--------|----------|-----------------------------------------------|
| vector_id  | string | required | The vector_id of the vector store to delete. |

### Response
| Name        | Type     | Description                                       |
|-------------|----------|---------------------------------------------------|
| vector_id   | string   | The unique identifier for the vector store. Will start with “KB-”. |

curl --request POST \
  --url https://kb.bland.ai/vectors/{vector_id}/delete \
  --header 'authorization: <authorization>'

RESPONSE

{
    "vector_id": "KB-55e64dae-1585-4632-ae97-c909c288c6bc"
}


CURL 
curl --request POST \
  --url https://kb.bland.ai/vectors/{vector_id}/delete \
  --header 'authorization: <authorization>'

RESPONSE 
{
  "message": "Vector deleted"
}


# Conversational Pathways
## Get All Pathways Information
Returns a set of information about all the conversational pathways in your account - including the name, description, nodes and edges.

### GET
`/v1/pathway`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Response
| Name        | Type                | Description                                       |
|-------------|---------------------|---------------------------------------------------|
| name        | string              | The name of the conversational pathway.           |
| description | string              | A description of the conversational pathway.     |
| nodes       | array of objects    | Data about all the nodes in the pathway.         |

#### Examples of JSON objects for nodes (Horizontal scroll the tab bar to see more examples)

**Start Node**
  {
      "id": "1",
      "type": "Default"
      "data": {
          "name": "Start",
          "text": "Hey there, how are you doing today?",
          "isStart": true,
      },
  


**Default Node**
  {
      "id": "randomnode_1710288871721",
      "type": "Default"
      "data": {
          "name": "New Node",
          "text": "Select a node or edge and press backspace to remove it",
          "globalPrompt": "This is a phone call. Do not use exclamation marks.\n\nConvert 24HR format timings to 12 HR format - e.g 14:00 should be written as 2 PM.",
      },
  }

**End Node**
{
    "id": "randomnode_1710288752186",
    "type": "End Call"
    "data": {
        "name": "End call",
        "prompt": "Say goodbye to the user",
    },
}

**Webhook Node**
{
    "id": "randomnode_1710288752186",
    "type": "Webhook",
    "data": {
        "url": "https://api.bland.ai/reservation",
        "body": "{\n    \"date\" : \"{{date}}\",\n    \"time\" : \"{{time}}\",\n    \"guests\": {{number_of_people}}\n}",
        "name": "Reservation Booking",
        "text": "Please give me a moment as I check our bookings..",
        "method": "POST",
        "extractVars": [
            [
                "date",
                "string",
                "Desired Date of reservation, in MM/DD/YYYY format"
            ],
            [
                "time",
                "string",
                "Desired Time of Reservation in 24HR Format e.g 13:30"
            ],
            [
                "number_of_people",
                "integer",
                "Number of people for the reservation"
            ]
        ],
        "responseData": [
            {
                "data": "$.reserved",
                "name": "reservation_success",
                "context": ""
            },
            {
                "data": "$.available_slots",
                "name": "available_slots",
                "context": "Available slots for the date provided"
            }
        ],
        "responsePathways": [
            [
                "reservation_success",
                "==",
                "true",
                {
                    "id": "randomnode_1710288752186",
                    "name": "Reservation Successful"
                }
            ],
            [
                "reservation_success",
                "==",
                "false",
                {
                    "id": "randomnode_1712265110018",
                    "name": "Find new timeslot"
                }
            ]
        ]
    }
}

**Knowledge Base Node**
{
    "id": "randomnode_1710288752186",
    "type": "Knowledge Base",
    "data": {
        "name": "Restaurant Questions",
        "prompt": "Answer any questions that the user may have regarding the restaurant, by referring to the knowledge base you have. \n\nAnswer the question in 1 line, and then ask if they have any more questions."
        "kb": "Opening Hours : 9am - 5pm\nStore Locations : \n426 Ivy Street San Francisco, \nSan Jose"
    }
}

**Global Node**
{
    "id": "randomnode_1710288871721",
    "type": "Default"
    "data": {
        "name": "Answer any questions",
        "prompt": "You are to answer any questions the user has.",
        "isGlobal": true,
        "globalLabel": "user asks a question"
    },
}

**Transfer Call Node**
{
    "id": "randomnode_1710288752186",
    "type": "Transfer Call",
    "data": {
        "name": "Transferring the call",
        "text": "Transferring the call now. Please hold.."
        "transferNumber": "+19547951234"
    }
}


## Node Data Object Parameters

- **name** — name of the node
- **isStart** — whether the node is the start node. There can only be 1 start node in a pathway. Either true or false.
- **isGlobal** — whether the node is a global node. Global nodes are nodes that can be used in multiple pathways. Either true or false.
- **globalLabel** — the label of the global node. Should be present if isGlobal is true.
- **type** — Type of the node. Can be Default, End Call, Transfer Node, Knowledge Base, or Webhook.
- **text** — If static text is chosen, this is the text that will be said to the user.
- **prompt** — If dynamic text is chosen, this is the prompt that will be shown to the user.
- **condition** — The condition that needs to be met to proceed from this node.
- **transferNumber** — If the node is a transfer node, this is the number to which the call will be transferred.
- **kb** — If the node is a knowledge base node, this is the knowledge base that will be used.
- **pathwayExamples** — The fine-tuning examples for the agent at this node for the pathways chosen.
- **conditionExamples** — The fine-tuning examples for the condition at this node for the condition chosen.
- **dialogueExamples** — The fine-tuning examples for the dialogue at this node for the dialogue chosen.
- **modelOptions**
  - **interruptionThreshold** — The sensitivity to interruptions at this node.
  - **temperature** — The temperature of the model.
- **extractVars** — An array of array of strings. [[varName, varType, varDescription]] e.g [["name", "string", "The name of the user"], ["age", "integer", "The age of the user"]]

### edges
- **array of objects** — Data about all the edges in the pathway.

## Edge Object Parameters

- **id** — unique id of the edge
- **source** — id of the source node
- **target** — id of the target node
- **label** — Label for this edge. This is what the agent will use to decide which path to take.


CURL 
curl --request GET \
  --url https://api.bland.ai/v1/pathway \
  --header 'authorization: <authorization>'

RESPONSE

{
  "name": "Default Demo Pathway",
  "description": null,
  "nodes": [
    {
      "id": "1",
      "data": {
        "name": "Start",
        "text": "Hey there, how are you doing today?",
        "isStart": true,
      },
      "type": "Default"
    },
    {
      "id": "randomnode_1710288752186",
      "data": {
        "name": "End call",
        "prompt": "Click 'Add New Node' on the right to add a new node",
      },
      "type": "End Call"
    },
    {
      "id": "randomnode_1710288871721",
      "data": {
        "name": "New Node",
        "text": "Select a node or edge and press backspace to remove it",
      },
      "type": "Default"
    },
    {
      "id": "randomnode_test123",
      "data": {
        "name": "Testing node",
        "text": "Hello there"
      },
      "type": "Default"
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-1-randomnode_1710288752186",
      "label": "greeted",
      "source": "1",
      "target": "randomnode_1710288752186"
    },
    {
      "id": "reactflow__edge-1-randomnode_1710288871721",
      "label": "New Edge",
      "source": "1",
      "target": "randomnode_1710288871721"
    }
  ]
}


## Conversational Pathways
### Get Single Pathway Information
Returns a set of information about the conversational pathway in your account - including the name, description, nodes and edges.

**GET**  
`/v1/pathway/{pathway_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | *        | Enter pathway_id                             |

### Headers
#### authorization
- **Type**: string  
- **Required**: Yes  
- **Description**: Your API key for authentication.

### Path Parameters
#### pathway_id
- **Type**: string  
- **Required**: Yes  
- **Description**: The unique identifier of the conversational pathway for which you want to retrieve detailed information.

### Response
| Name        | Type              | Description                                       |
|-------------|-------------------|---------------------------------------------------|
| name        | string            | The name of the conversational pathway.           |
| description | string            | A description of the conversational pathway.     |
| nodes       | array of objects   | Data about all the nodes in the pathway.         |

Examples of JSON objects for nodes (Horizontal scroll the tab bar to see more examples)

Start Node

  {
      "id": "1",
      "type": "Default"
      "data": {
          "name": "Start",
          "text": "Hey there, how are you doing today?",
          "isStart": true,
      },

Default Node

  {
      "id": "randomnode_1710288871721",
      "type": "Default"
      "data": {
          "name": "New Node",
          "text": "Select a node or edge and press backspace to remove it",
          "globalPrompt": "This is a phone call. Do not use exclamation marks.\n\nConvert 24HR format timings to 12 HR format - e.g 14:00 should be written as 2 PM.",
      },
  }


End Node

{
    "id": "randomnode_1710288752186",
    "type": "End Call"
    "data": {
        "name": "End call",
        "prompt": "Say goodbye to the user",
    },
}


Webhook Node

{
    "id": "randomnode_1710288752186",
    "type": "Webhook",
    "data": {
        "url": "https://api.bland.ai/reservation",
        "body": "{\n    \"date\" : \"{{date}}\",\n    \"time\" : \"{{time}}\",\n    \"guests\": {{number_of_people}}\n}",
        "name": "Reservation Booking",
        "text": "Please give me a moment as I check our bookings..",
        "method": "POST",
        "extractVars": [
            [
                "date",
                "string",
                "Desired Date of reservation, in MM/DD/YYYY format"
            ],
            [
                "time",
                "string",
                "Desired Time of Reservation in 24HR Format e.g 13:30"
            ],
            [
                "number_of_people",
                "integer",
                "Number of people for the reservation"
            ]
        ],
        "responseData": [
            {
                "data": "$.reserved",
                "name": "reservation_success",
                "context": ""
            },
            {
                "data": "$.available_slots",
                "name": "available_slots",
                "context": "Available slots for the date provided"
            }
        ],
        "responsePathways": [
            [
                "reservation_success",
                "==",
                "true",
                {
                    "id": "randomnode_1710288752186",
                    "name": "Reservation Successful"
                }
            ],
            [
                "reservation_success",
                "==",
                "false",
                {
                    "id": "randomnode_1712265110018",
                    "name": "Find new timeslot"
                }
            ]
        ]
    }
}


Knowledge Base Node

{
    "id": "randomnode_1710288752186",
    "type": "Knowledge Base",
    "data": {
        "name": "Restaurant Questions",
        "prompt": "Answer any questions that the user may have regarding the restaurant, by referring to the knowledge base you have. \n\nAnswer the question in 1 line, and then ask if they have any more questions."
        "kb": "Opening Hours : 9am - 5pm\nStore Locations : \n426 Ivy Street San Francisco, \nSan Jose"
    }
}


Global Node

{
    "id": "randomnode_1710288871721",
    "type": "Default"
    "data": {
        "name": "Answer any questions",
        "prompt": "You are to answer any questions the user has.",
        "isGlobal": true,
        "globalLabel": "user asks a question"
    },
}


Transfer Call Node

{
    "id": "randomnode_1710288752186",
    "type": "Transfer Call",
    "data": {
        "name": "Transferring the call",
        "text": "Transferring the call now. Please hold.."
        "transferNumber": "+19547951234"
    }
}

## Node Data Object Parameters

- **name** — name of the node
- **isStart** — whether the node is the start node. There can only be 1 start node in a pathway. Either true or false.
- **isGlobal** — whether the node is a global node. Global nodes are nodes that can be used in multiple pathways. Either true or false.
- **globalLabel** — the label of the global node. Should be present if isGlobal is true.
- **type** — Type of the node. Can be Default, End Call, Transfer Node, Knowledge Base, or Webhook.
- **text** — If static text is chosen, this is the text that will be said to the user.
- **prompt** — If dynamic text is chosen, this is the prompt that will be shown to the user.
- **condition** — The condition that needs to be met to proceed from this node.
- **transferNumber** — If the node is a transfer node, this is the number to which the call will be transferred.
- **kb** — If the node is a knowledge base node, this is the knowledge base that will be used.
- **pathwayExamples** — The fine-tuning examples for the agent at this node for the pathways chosen.
- **conditionExamples** — The fine-tuning examples for the condition at this node for the condition chosen.
- **dialogueExamples** — The fine-tuning examples for the dialogue at this node for the dialogue chosen.
- **modelOptions**
  - **interruptionThreshold** — The sensitivity to interruptions at this node.
  - **temperature** — The temperature of the model.
- **extractVars** — An array of array of strings. `[[varName, varType, varDescription]]` e.g `[['name', 'string', 'The name of the user'], ['age', 'integer', 'The age of the user']]`

- **edges** — array of objects. Data about all the edges in the pathway.

### Edge Object Parameters

- **id** — unique id of the edge
- **source** — id of the source node
- **target** — id of the target node
- **label** — Label for this edge. This is what the agent will use to decide which path to take.


cURL 
curl --request GET \
  --url https://api.bland.ai/v1/pathway/{pathway_id} \
  --header 'authorization: <authorization>'

RESPONSE

{
  "name": "Default Demo Pathway",
  "description": null,
  "nodes": [
    {
      "id": "1",
      "data": {
        "name": "Start",
        "text": "Hey there, how are you doing today?",
        "isStart": true,
      },
      "type": "Default"
    },
    {
      "id": "randomnode_1710288752186",
      "data": {
        "name": "End call",
        "prompt": "Click 'Add New Node' on the right to add a new node",
      },
      "type": "End Call"
    },
    {
      "id": "randomnode_1710288871721",
      "data": {
        "name": "New Node",
        "text": "Select a node or edge and press backspace to remove it",
      },
      "type": "Default"
    },
    {
      "id": "randomnode_test123",
      "data": {
        "name": "Testing node",
        "text": "Hello there"
      },
      "type": "Default"
    }
  ],
  "edges": [
    {
      "id": "reactflow__edge-1-randomnode_1710288752186",
      "label": "greeted",
      "source": "1",
      "target": "randomnode_1710288752186"
    },
    {
      "id": "reactflow__edge-1-randomnode_1710288871721",
      "label": "New Edge",
      "source": "1",
      "target": "randomnode_1710288871721"
    }
  ]
}


# Conversational Pathways
## Create Pathway
Create a new conversational pathway

**POST**  
`/v1/pathway/create`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| name        | string | *        | Enter name                                    |
| description | string |          | Enter description                             |

### Headers
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Body
| Name        | Type     | Required | Description                                       |
|-------------|----------|----------|---------------------------------------------------|
| name        | string   | required | The name of the conversational pathway you want to create |
| description | string   |          | A description of the conversational pathway you want to create |

### Response
| Name       | Type     | Description                                       |
|------------|----------|---------------------------------------------------|
| status     | string   | Can be success or error.                         |
| pathway_id | string   | A unique identifier for the pathway (present only if status is success). |


CURL
curl --request POST \
  --url https://api.bland.ai/v1/pathway/create \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>"
}'

RESPONSE
{
  "status": "success",
  "pathway_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1"
}

**Conversational Pathways**  
### Update Pathway
Update a conversational pathway’s fields - including name, description, nodes and edges.

**POST**  
`/v1/pathway/{pathway_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | *        | Enter pathway_id                             |

### Body
| Name        | Type              | Required | Description                                   |
|-------------|-------------------|----------|-----------------------------------------------|
| name        | string            | *        | Enter name                                    |
| description | string            |          | Enter description                             |
| nodes       | array of objects   |          | Data about all the nodes in the pathway.     |
| edges       | object            |          | Data about the edges in the pathway.         |

### Headers
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Path Parameters
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | required | The unique identifier of the conversational pathway you want to update. |

### Body
| Name        | Type              | Description                                   |
|-------------|-------------------|-----------------------------------------------|
| name        | string            | The name of the conversational pathway        |
| description | string            | A description of the pathway                  |
| nodes       | array of objects   | Data about all the nodes in the pathway.     |

Example of a node object:


Start Node

  {
      "id": "1",
      "type": "Default"
      "data": {
          "name": "Start",
          "text": "Hey there, how are you doing today?",
          "isStart": true,
      },
  

Default Node

  {
      "id": "randomnode_1710288871721",
      "type": "Default"
      "data": {
          "name": "New Node",
          "text": "Select a node or edge and press backspace to remove it",
          "globalPrompt": "This is a phone call. Do not use exclamation marks.\n\nConvert 24HR format timings to 12 HR format - e.g 14:00 should be written as 2 PM.",
      },
  }


End Node

{
    "id": "randomnode_1710288752186",
    "type": "End Call"
    "data": {
        "name": "End call",
        "prompt": "Say goodbye to the user",
    },
}


Webhook Node

{
    "id": "randomnode_1710288752186",
    "type": "Webhook",
    "data": {
        "url": "https://api.bland.ai/reservation",
        "body": "{\n    \"date\" : \"{{date}}\",\n    \"time\" : \"{{time}}\",\n    \"guests\": {{number_of_people}}\n}",
        "name": "Reservation Booking",
        "text": "Please give me a moment as I check our bookings..",
        "method": "POST",
        "extractVars": [
            [
                "date",
                "string",
                "Desired Date of reservation, in MM/DD/YYYY format"
            ],
            [
                "time",
                "string",
                "Desired Time of Reservation in 24HR Format e.g 13:30"
            ],
            [
                "number_of_people",
                "integer",
                "Number of people for the reservation"
            ]
        ],
        "responseData": [
            {
                "data": "$.reserved",
                "name": "reservation_success",
                "context": ""
            },
            {
                "data": "$.available_slots",
                "name": "available_slots",
                "context": "Available slots for the date provided"
            }
        ],
        "responsePathways": [
            [
                "reservation_success",
                "==",
                "true",
                {
                    "id": "randomnode_1710288752186",
                    "name": "Reservation Successful"
                }
            ],
            [
                "reservation_success",
                "==",
                "false",
                {
                    "id": "randomnode_1712265110018",
                    "name": "Find new timeslot"
                }
            ]
        ]
    }
}


Knowledge Base Node

{
    "id": "randomnode_1710288752186",
    "type": "Knowledge Base",
    "data": {
        "name": "Restaurant Questions",
        "prompt": "Answer any questions that the user may have regarding the restaurant, by referring to the knowledge base you have. \n\nAnswer the question in 1 line, and then ask if they have any more questions."
        "kb": "Opening Hours : 9am - 5pm\nStore Locations : \n426 Ivy Street San Francisco, \nSan Jose"
    }
}


Global Node

{
    "id": "randomnode_1710288871721",
    "type": "Default"
    "data": {
        "name": "Answer any questions",
        "prompt": "You are to answer any questions the user has.",
        "isGlobal": true,
        "globalLabel": "user asks a question"
    },
}


Transfer Call Node

{
    "id": "randomnode_1710288752186",
    "type": "Transfer Call",
    "data": {
        "name": "Transferring the call",
        "text": "Transferring the call now. Please hold.."
        "transferNumber": "+19547951234"
    }
}


### Node Data Object Parameters

- **name** — name of the node
- **isStart** — whether the node is the start node. There can only be 1 start node in a pathway. Either true or false.
- **isGlobal** — whether the node is a global node. Global nodes are nodes that can be used in multiple pathways. Either true or false.
- **globalLabel** — the label of the global node. Should be present if isGlobal is true.
- **type** — Type of the node. Can be Default, End Call, Transfer Node, Knowledge Base, or Webhook.
- **text** — If static text is chosen, this is the text that will be said to the user.
- **prompt** — If dynamic text is chosen, this is the prompt that will be shown to the user.
- **condition** — The condition that needs to be met to proceed from this node.
- **transferNumber** — If the node is a transfer node, this is the number to which the call will be transferred.
- **kb** — If the node is a knowledge base node, this is the knowledge base that will be used.
- **pathwayExamples** — The fine-tuning examples for the agent at this node for the pathways chosen.
- **conditionExamples** — The fine-tuning examples for the condition at this node for the condition chosen.
- **dialogueExamples** — The fine-tuning examples for the dialogue at this node for the dialogue chosen.
- **modelOptions**
  - **modelName** — The name of the model to be used for this node.
  - **interruptionThreshold** — The sensitivity to interruptions at this node.
  - **temperature** — The temperature of the model.
- **extractVars** — An array of array of strings. `[[varName, varType, varDescription]]` e.g `[['name', 'string', 'The name of the user'], ['age', 'integer', 'The age of the user']]`
- **edges** — array of objects. Data about all the edges in the pathway.

### Edge Object Parameters

- **id** — unique id of the edge.
- **source** — id of the source node.
- **target** — id of the target node.
- **label** — Label for this edge. This is what the agent will use to decide which path to take.

### Response

- **status** — string. Can be success or error.
- **pathway_id** — string. A unique identifier for the pathway (present only if status is success).
- **nodes** — array of objects. Data about all the nodes in the pathway.
- **edges** — array of objects. Data about all the edges in the pathway.

CURL
curl --request POST \
  --url https://api.bland.ai/v1/pathway/{pathway_id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>",
  "nodes": {},
  "edges": {}
}'

RESPONSE
{
  "status": "success",
  "message": "Pathway updated successfully",
  "pathway_data": {
    "pathway_id": "9d404c1b-6a23-4426-953a-a52c392ff8f1",
    "name": "Updated Demo Pathway",
    "description": "This is an updated description",
    "nodes": [
        {
            "id": "1",
            "data": {
                "name": "Start",
                "text": "Hey there, how are you doing today?",
                "isStart": true,
            },
            "type": "Default"
        },
        {
            "id": "randomnode_1710288752186",
            "data": {
                "name": "End call",
                "prompt": "Click 'Add New Node' on the right to add a new node",
            },
            "type": "End Call"
        },
        {
            "id": "randomnode_1710288871721",
            "data": {
                "name": "New Node",
                "prompt": "Click 'Add New Node' on the right to add a new node",
            },
            "type": "Default"
        }
    ],
    "edges": [
        {
            "id": "1",
            "source": "1",
            "target": "randomnode_1710288752186",
            "data": {
                "name": "End call",
                "prompt": "Click 'Add New Node' on the right to add a new node",
            }
        },
        {
            "id": "2",
            "source": "1",
            "target": "randomnode_1710288871721",
            "data": {
                "name": "New Node",
                "prompt": "Click 'Add New Node' on the right to add a new node",
            }
        }
    ]
  }
}

### Conversational Pathways
#### Delete Pathway
Delete your conversational pathway.

**DELETE**  
`/v1/pathway/{pathway_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | *        | Enter pathway_id                             |

### Headers
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Path Parameters
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | required | The unique identifier of the conversational pathway you want to delete. |

### Response
| Name        | Type   | Description                                       |
|-------------|--------|---------------------------------------------------|
| status      | string | Can be success or error.                         |
| pathway_id  | string | A unique identifier for the pathway (present only if status is success). |


CURL
curl --request DELETE \
  --url https://api.bland.ai/v1/pathway/{pathway_id} \
  --header 'authorization: <authorization>'

RE
{
  "status": "success",
  "message": "Pathway deleted successfully"
}

### Pathway Chat
#### Create Pathway Chat
Create an instance of a pathway chat, which can be used to send and receive messages to the pathway.

**POST**  
`/v1/pathway/chat/create`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name          | Type   | Description                                   |
|---------------|--------|-----------------------------------------------|
| pathway_id    | string | Enter pathway_id                             |
| start_node_id | string | Enter start_node_id                          |

### Headers
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Body
| Name          | Type   | Description                                   |
|---------------|--------|-----------------------------------------------|
| pathway_id    | string | Pathway ID of the pathway to create a chat instance for. |
| start_node_id | string | The start node ID of the pathway.            |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | Can be success or error.                         |
| chat_id   | uuid     | The ID of the chat instance created. This will be used to send and receive messages to the pathway via the `/pathway/chat` endpoint. |
| message   | string   | If the status is success, the message will say “Chat instance created successfully.” Otherwise, if the status is error, the message will say “Error creating chat instance.” |

CURL
curl --request POST \
  --url https://us.api.bland.ai/v1/pathway/chat/create \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "pathway_id": "<string>",
  "start_node_id": "<string>"
}'

RESPONSE
{
  "status": "success",
  "chat_id": "1234567890",
  "message": "Chat instance created successfully"
}

### Pathway Chat
Send a message to a pathway and receive a response.

**POST**  
`/v1/pathway/chat/{id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name | Type | Required | Description                       |
|------|------|----------|-----------------------------------|
| id   | string | *      | Enter id                          |

### Body
| Name    | Type   | Description                       |
|---------|--------|-----------------------------------|
| message | string | Enter message                     |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name | Type | Required | Description                                   |
|------|------|----------|-----------------------------------------------|
| id   | uuid | required | The chat ID created from the /pathway/chat/create endpoint. |

### Body
| Name    | Type   | Description                                   |
|---------|--------|-----------------------------------------------|
| message | string | The message to send to the pathway (optional) |

### Response
| Name              | Type     | Description                                       |
|-------------------|----------|---------------------------------------------------|
| status            | string   | Can be success or error.                         |
| chat_id           | uuid     | The ID of the chat instance created. This will be used to send and receive messages to the pathway via the /pathway/chat endpoint. |
| assistant_response | string   | The response from the Assistant to the message sent. |
| current_node_id   | string   | The ID of the current node in the pathway.      |
| current_node_name | string   | The name of the current node in the pathway.    |
| chat_history      | array    | An array of objects containing the role and content of each message in the chat. |
| pathway_id        | string   | The ID of the pathway the chat is associated with. |


curl --request POST \
  --url https://us.api.bland.ai/v1/pathway/chat/{id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "message": "<string>"
}'

RESPONSE

{
  "status": "success",
  "chat_id": "1234567890",
  "Assistant Response": "Hey there, how are you doing?",
  "Current Node ID": "node_123",
  "Current Node Name": "Welcome Node",
  "Chat History": [
    {"role": "user", "content": "Hello"}, {"role": "assistant", "content":  "Hi there!"}
  ],
  "Pathway ID": "pathway_123"
}


### Pathway Chat
Get conversation history for a pathway chat.

**GET**  
`/v1/pathway/chat/{id}`  
Send

### Header
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | *        | Enter authorization                           |

### Path
| Name | Type | Required | Description                                   |
|------|------|----------|-----------------------------------------------|
| id   | uuid | *        | Enter id                                     |

### Headers
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | required | Your API key for authentication.              |

### Path Parameters
| Name | Type | Required | Description                                   |
|------|------|----------|-----------------------------------------------|
| id   | uuid | required | The chat ID created from the /pathway/chat/create endpoint. |

### Response
| Name   | Type   | Description                                       |
|--------|--------|---------------------------------------------------|
| errors | array  | List of errors or null.                           |
| data   | array  | Message objects for the conversation history.     |


CURL
curl --request GET \
  --url https://us.api.bland.ai/v1/pathway/chat/{id} \
  --header 'authorization: <authorization>'

RESPONSE
{
  "errors": null,
  "data": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
  ]
}


CURL
curl --request GET \
  --url https://us.api.bland.ai/v1/pathway/chat/{id} \
  --header 'authorization: <authorization>'

REPSONSE
{
    data: [
        {
            "role": "user",
            "content": "message"
        },
        ... // more messages
    ]
}


### Pathway Versions
Get Pathway Versions
Retrieves all versions of a specific pathway, including version number, creation date, name, and latest status.

**GET**  
`/v1/pathway/{pathway_id}/versions`  
Send

### Header
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | *        | Enter authorization                           |

### Path
| Name        | Type   | Required | Description                                   |
|-------------|--------|----------|-----------------------------------------------|
| pathway_id  | string | *        | Enter pathway_id                              |

### Response
| Name            | Type     | Description                                       |
|-----------------|----------|---------------------------------------------------|
| id              | string   | The unique identifier of the pathway version.     |
| version_number  | integer  | The version number of this pathway version.       |
| created_at      | string   | The timestamp when this version was created.      |
| name            | string   | The name of this pathway version.                 |
| is_latest       | boolean  | Indicates whether this is the latest version of the pathway. |

### cURL
curl --request GET \
  --url https://api.bland.ai/v1/pathway/:pathway_id/versions \
  --header 'authorization: <authorization>'


RESPONSE
[
  {
    "id": "v1_abc123",
    "version_number": 1,
    "created_at": "2024-03-05T12:00:00Z",
    "name": "Initial Version",
    "is_latest": false
  },
  {
    "id": "v2_def456",
    "version_number": 2,
    "created_at": "2024-03-06T14:30:00Z",
    "name": "Updated Flow",
    "is_latest": true
  }
]



### Pathway Versions
#### Get Specific Pathway Version
Retrieves a specific version of a pathway, including its name, nodes, edges, version number, and latest status.

**GET**  
`/v1/pathway/{pathway_id}/version/{version_id}`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | *        | Enter pathway_id                              |
| version_id  | string   | *        | Enter version_id                              |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | required | The ID of the pathway.                        |
| version_id  | string   | required | The ID of the version to retrieve. Use 0 for the live pathway. |

### Response
| Name            | Type              | Description                                       |
|-----------------|-------------------|---------------------------------------------------|
| name            | string            | The name of the pathway version.                  |
| nodes           | array of objects   | Data about all the nodes in the pathway version.  |
| edges           | array of objects   | Data about all the edges in the pathway version.  |
| version_number  | integer           | The version number of this pathway version.       |
| is_latest       | boolean           | Indicates whether this is the latest version of the pathway. |

#### Node Object Parameters
| Name            | Type              | Description                                       |
|-----------------|-------------------|---------------------------------------------------|
| id              | string            | Unique identifier of the node                     |
| type            | string            | Type of the node (e.g., “Default”, “End Call”, “Webhook”) |
| data            | object            | Object containing node-specific data              |
| name            | string            | Name of the node                                  |
| text or prompt  | string            | Text or prompt associated with the node          |
| Other properties specific to the node type | various | Additional properties depending on node type |

#### Edge Object Parameters
| Name            | Type              | Description                                       |
|-----------------|-------------------|---------------------------------------------------|
| id              | string            | Unique identifier of the edge                     |
| source          | string            | ID of the source node                             |
| target          | string            | ID of the target node                             |
| label           | string            | Label for this edge                               |

### cURL
curl --request GET \
  --url https://api.bland.ai/v1/pathway/{pathway_id}/version/{version_id} \
  --header 'authorization: <authorization>'

RESPONSE
{
  "name": "Customer Support Flow v2",
  "nodes": [
    {
      "id": "1",
      "type": "Default",
      "data": {
        "name": "Start",
        "text": "Hello! How can I assist you today?",
        "isStart": true
      }
    },
    {
      "id": "2",
      "type": "End Call",
      "data": {
        "name": "End call",
        "prompt": "Thank you for contacting us. Have a great day!"
      }
    }
  ],
  "edges": [
    {
      "id": "edge-1-2",
      "source": "1",
      "target": "2",
      "label": "Issue resolved"
    }
  ],
  "version_number": 2,
  "is_latest": true
}


### Pathway Versions
#### Promote Pathway Version
Promote a pathway version for a pathway ID to either staging or production environment.

**POST**  
`/v1/pathway/{pathway_id}/publish`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | *        | Enter pathway_id                             |

### Body
| Name        | Type     | Description                                   |
|-------------|----------|-----------------------------------------------|
| version_id  | number   | Enter version_id                              |
| environment  | string   | The environment you want to promote the pathway to. Can be production or staging. Default is production. |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | required | The ID of the pathway you want to promote.   |

### Body
| Name        | Type     | Description                                   |
|-------------|----------|-----------------------------------------------|
| version_id  | number   | The version number of the pathway you want to promote. |
| environment  | string   | The environment you want to promote the pathway to. Can be production or staging. Default is production. |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| message   | string   | A message indicating the status of the request.   |


CURL
curl --request POST \
  --url https://api.bland.ai/v1/pathway/{pathway_id}/publish \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "version_id": 123,
  "environment": "<string>"
}'

RESPONSE
{
  "message": "Pathway published successfully"
}


### Create Pathway Version
Creates a new version of a specific pathway, including its name, nodes, and edges.

**POST**  
`/v1/pathway/{pathway_id}/version`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | *        | Enter pathway_id                             |

### Body
| Name        | Type               | Description                                   |
|-------------|--------------------|-----------------------------------------------|
| name        | string             | Enter name                                    |
| nodes       | array of objects    | An array of node objects defining the structure of the pathway. |
| edges       | array of objects    | An array of edge objects defining the connections between nodes. |

#### Node Object Parameters
| Name        | Type               | Description                                   |
|-------------|--------------------|-----------------------------------------------|
| id          | string             | Unique identifier of the node                 |
| type        | string             | Type of the node (e.g., “Default”, “End Call”, “Webhook”) |
| data        | object             | Object containing node-specific data          |
| name        | string             | Name of the node                              |
| text/prompt | string             | Text or prompt associated with the node      |
| Other properties specific to the node type | - | - |

#### Edge Object Parameters
| Name        | Type               | Description                                   |
|-------------|--------------------|-----------------------------------------------|
| id          | string             | Unique identifier of the edge                 |
| source      | string             | ID of the source node                         |
| target      | string             | ID of the target node                         |
| label       | string             | Label for this edge                           |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | The status of the operation (e.g., “success”).   |
| message   | string   | A message describing the result of the operation. |
| data      | object   | -                                                 |
| created_at| string   | The timestamp when the new version was created.   |
| id        | string   | The unique identifier of the newly created version. |
| name      | string   | The name of the newly created version.            |
| version_number | integer  | The version number of the newly created version. |

CURL
curl --request POST \
  --url https://api.bland.ai/v1/pathway/{pathway_id}/version \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "nodes": {},
  "edges": {}
}'

RESPOONSE
{
  "status": "success",
  "message": "Version created successfully",
  "data": {
    "created_at": "2024-03-07T10:15:30Z",
    "id": "v3_ghi789",
    "name": "Improved Customer Flow",
    "version_number": 3
  }
}

### Delete Pathway Version
Marks a specific version of a pathway as archived, effectively deleting it from active use.

**DELETE**  
`/v1/pathway/{pathway_id}/version/{version_id}`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | *        | Enter pathway_id                              |
| version_id   | string   | *        | Enter version_id                              |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | required | The ID of the pathway containing the version to be deleted. |
| version_id   | string   | required | The ID of the version to be deleted.         |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | The status of the operation (e.g., “success”).   |
| message   | string   | A message describing the result of the operation. |

CURL
curl --request DELETE \
  --url https://api.bland.ai/v1/pathway/{pathway_id}/version/{version_id} \
  --header 'authorization: <authorization>'

RESPONSE
{
  "status": "success",
  "message": "Version deleted successfully"
}


### Pathway Folders
#### Get All Folders
Retrieves all folders for the authenticated user, including folder ID, name, and parent folder ID.

**GET**  
`/v1/pathway/folders`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Response
| Name    | Type   | Description                                       |
|---------|--------|---------------------------------------------------|
| folders | array  | An array of folder objects.                       |

| folders[].id           | string | The unique identifier of the folder.              |
| folders[].name         | string | The name of the folder.                           |
| folders[].parent_folder_id | string | The ID of the parent folder, if applicable.   |

CURL
curl --request GET \
  --url https://us.api.bland.ai/v1/pathway/folders \
  --header 'authorization: <authorization>'

RESPONSE
{
  "folders": [
    {
      "id": "folder_123",
      "name": "My Folder",
      "parent_folder_id": null
    },
    {
      "id": "folder_456",
      "name": "Subfolder",
      "parent_folder_id": "folder_123"
    }
  ]
}


### Pathway Folders
#### Get Pathways in Folder
Retrieves all pathways within a specific folder for the authenticated user.

**GET**  
`/v1/pathway/folders/{folder_id}/pathways`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| folder_id | string   | *        | Enter folder_id                              |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| folder_id | string   | required | The ID of the folder to retrieve pathways from. |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| pathways  | array    | An array of pathway objects within the specified folder. |

| pathways[].id           | string | The unique identifier of the pathway.              |
| pathways[].name         | string | The name of the pathway.                           |
| pathways[].description  | string | The description of the pathway.                    |
| pathways[].created_at   | string | The creation date and time of the pathway.        |

### cURL

curl --request GET \
  --url https://us.api.bland.ai/v1/pathway/folders/{folder_id}/pathways \
  --header 'authorization: <authorization>'

RESPONSE
{
  "pathways": [
    {
      "id": "pathway_123",
      "name": "Customer Support Flow",
      "description": "A flow for customer support interactions.",
      "created_at": "2024-03-05T12:00:00Z"
    },
    {
      "id": "pathway_456",
      "name": "Sales Process",
      "description": "A flow for managing sales interactions.",
      "created_at": "2024-03-06T14:30:00Z"
    }
  ]
}


RESPONSE
{
  "pathways": [
    {
      "id": "pathway_123",
      "name": "My Pathway",
      "description": "A sample pathway",
      "created_at": "2024-03-15T12:00:00Z"
    }
  ]
}


# Pathway Folders
## Create Folder
Creates a new folder for the authenticated user.

**POST**  
`/v1/pathway/folders`  
Send

### Header
| Name              | Type     | Required | Description                          |
|-------------------|----------|----------|--------------------------------------|
| authorization     | string   | *        | Enter authorization                  |

### Body
| Name              | Type     | Required | Description                                   |
|-------------------|----------|----------|-----------------------------------------------|
| name              | string   | *        | Enter name                                   |
| parent_folder_id  | string   |          | Enter parent_folder_id                       |

### Headers
| Name              | Type     | Required | Description                                   |
|-------------------|----------|----------|-----------------------------------------------|
| authorization     | string   | required | Your API key for authentication.              |

### Body Parameters
| Name              | Type     | Required | Description                                   |
|-------------------|----------|----------|-----------------------------------------------|
| name              | string   | required | The name of the new folder.                  |
| parent_folder_id  | string   |          | The ID of the parent folder, if creating a subfolder. |

### Response
| Name              | Type     | Description                                       |
|-------------------|----------|---------------------------------------------------|
| folder_id         | string   | The unique identifier of the newly created folder. |
| name              | string   | The name of the newly created folder.             |
| parent_folder_id  | string   | The ID of the parent folder, if applicable.       |


cURL
curl --request POST \
  --url https://us.api.bland.ai/v1/pathway/folders \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "parent_folder_id": "<string>"
}'

Response

{
  "folder_id": "new_folder_123",
  "name": "New Folder",
  "parent_folder_id": null
}


# Start Generation Here
### Pathway Folders
#### Delete Folder
Deletes a specific folder for the authenticated user. The folder must be empty to be deleted.

**DELETE**  
`/v1/pathway/folders/{folder_id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name      | Type   | Required | Description                                   |
|-----------|--------|----------|-----------------------------------------------|
| folder_id | string | *        | Enter folder_id                             |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name      | Type   | Required | Description                                   |
|-----------|--------|----------|-----------------------------------------------|
| folder_id | string | required | The ID of the folder to delete.              |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| folder_id | string   | The ID of the deleted folder.                     |


cURL
curl --request DELETE \
  --url https://us.api.bland.ai/v1/pathway/folders/{folder_id} \
  --header 'authorization: <authorization>'

Response
{
  "folder_id": "deleted_folder_123"
}


### Pathway Folders
#### Update Folder
Updates the name of a specific folder for the authenticated user.

**PATCH**  
`/v1/pathway/folders/{folder_id}`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| folder_id | string   | *        | Enter folder_id                             |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| folder_id | string   | required | The ID of the folder to update.              |

### Body Parameters
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| name      | string   | required | The new name for the folder.                 |

### Response
| Name            | Type     | Description                                       |
|-----------------|----------|---------------------------------------------------|
| folder_id       | string   | The unique identifier of the updated folder.      |
| name            | string   | The updated name of the folder.                   |
| parent_folder_id| string   | The ID of the parent folder, if applicable.       |


cURL
curl --request PATCH \
  --url https://us.api.bland.ai/v1/pathway/folders/{folder_id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>"
}'

Response
{
  "folder_id": "updated_folder_123",
  "name": "New Folder Name",
  "parent_folder_id": null
}


# Start Generation Here
### Pathway Folders
#### Move Pathway
Moves a pathway to a different folder or to the root level.

**POST**  
`/v1/pathway/folders/move`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | *        | Enter pathway_id                             |
| folder_id   | string   |          | Enter folder_id (if null, moves to root)   |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Body Parameters
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| pathway_id  | string   | required | The ID of the pathway to move.                |
| folder_id   | string   |          | The ID of the destination folder. If null, the pathway will be moved to the root level. |

### Response
| Name            | Type     | Description                                       |
|-----------------|----------|---------------------------------------------------|
| pathway_id      | string   | The ID of the moved pathway.                      |
| old_folder_id   | string   | The ID of the original folder.                    |
| new_folder_id   | string   | The ID of the new folder, or null if moved to root level. |

### cURL
curl --request POST \
  --url https://us.api.bland.ai/v1/pathway/folders/move \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "pathway_id": "<string>",
  "folder_id": "<string>"
}'

Response
{
  "pathway_id": "moved_pathway_123",
  "old_folder_id": "original_folder_456",
  "new_folder_id": "new_folder_789"
}


### Inbound Numbers
#### Purchase Phone Number
Purchase a new phone number (inbound/outbound). ($15/mo. subscription using your stored payment method).

**POST**  
`/numbers/purchase`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Body
| Name          | Type   | Description                                   |
|---------------|--------|-----------------------------------------------|
| area_code     | string | Enter area_code                              |
| country_code   | string | Enter country_code                           |
| phone_number  | string | Enter phone_number                           |

### cURL
curl --request POST \
  --url https://api.bland.ai/numbers/purchase \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "area_code": "<string>",
  "country_code": "<string>",
  "phone_number": "<string>"
}'

### Inbound Numbers
#### Update Inbound Details
Update your inbound agent’s settings, prompt and other details.

**POST**  
`/v1/inbound/{phone_number}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |
| encrypted_key | string |          | Enter encrypted_key                  |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| phone_number| string   | *        | Enter phone_number                            |

### Body
| Name                | Type     | Description                                   |
|---------------------|----------|-----------------------------------------------|
| prompt              | string   | * Enter prompt                                |
| pathway_id          | string   | Enter pathway_id                              |
| voice               | string   | Enter voice                                   |
| background_track    | string   | Enter background_track                        |
| first_sentence      | string   | Enter first_sentence                          |
| wait_for_greeting   | boolean  | Select option                                 |
| interruption_threshold | number | Enter interruption_threshold                  |
| model               | string   | Enter model                                   |
| tools               | array    |                                               |
| language            | string   | Enter language                                |
| timezone            | string   | Enter timezone                                |
| transfer_phone_number| string  | Enter transfer_phone_number                   |
| transfer_list       | object   |                                               |
| dynamic_data        | object   |                                               |
| keywords            | array    |                                               |
| max_duration        | integer  | Enter max_duration                            |
| webhook             | string   | Enter webhook                                 |
| analysis_schema     | object   |                                               |
| metadata            | object   |                                               |
| summary_prompt      | string   | Enter summary_prompt                          |
| analysis_prompt     | string   | Enter analysis_prompt                         |
| record              | boolean  | Select option                                 |

### Response
| Name              | Type     | Description                                       |
|-------------------|----------|---------------------------------------------------|
| status            | string   | Whether the update was successful or not - will be success or error. |
| message           | string   | A message describing the status of the update.   |
| updates           | object   | An object containing the updated settings for the inbound number. |
| failed_updates     | object   | If the update was unsuccessful, this will contain the settings that failed to update. Useful to determine how your request is being interpreted on our end. 

cURL
curl --request POST \
  --url https://api.bland.ai/v1/inbound/{phone_number} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "prompt": "<string>",
  "pathway_id": "<string>",
  "voice": "<string>",
  "background_track": "<string>",
  "first_sentence": "<string>",
  "wait_for_greeting": true,
  "interruption_threshold": 123,
  "model": "<string>",
  "tools": [
    {}
  ],
  "language": "<string>",
  "timezone": "<string>",
  "transfer_phone_number": "<string>",
  "transfer_list": {},
  "dynamic_data": {},
  "keywords": [
    "<string>"
  ],
  "max_duration": 123,
  "webhook": "<string>",
  "analysis_schema": {},
  "metadata": {},
  "summary_prompt": "<string>",
  "analysis_prompt": "<string>",
  "record": true
}'

Response
{
    "status": "success",
    "message": "Successfully updated number +18584139939.",
    "updates": {
        "prompt": "(Your prompt)",
        "voice": "maya",
        "webhook": null,
        "first_sentence": "Roberta speaking, how can I help you?",
        "record": false,
        "max_duration": 30,
        "model": "enhanced",
        //...
    }
}


### Inbound Numbers
#### List Inbound Numbers
Retrieves a list of all inbound phone numbers configured for your account, along with their associated settings.

**GET**  
`/v1/inbound`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |
| encrypted_key | string   |          | Enter encrypted_key                           |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |
| encrypted_key | string   |          | Use your own Twilio account and only return inbound numbers associated with that account sid (optional). |

### Response
| Name            | Type              | Description                                       |
|-----------------|-------------------|---------------------------------------------------|
| inbound_numbers  | array of objects   | An array of objects, each representing an inbound phone number and its configuration. |

### cURL
curl --request GET \
  --url https://api.bland.ai/v1/inbound \
  --header 'authorization: <authorization>'

RESPONSE
{
    "inbound_numbers": [
        {
            "created_at": "2023-11-27T17:21:38.33359+00:00",
            "phone_number": "+18005551234",
            "prompt": "When you receive a call, recite a random poem from 'Sunset Boulevard' and then ask, 'How may I assist you in your poetic journey today?'",
            "webhook": "https://api.example.com/poetry-line",
            "voice_id": 2,
            "dynamic_data": [/* Use [Dynamic Data](/api-reference/endpoint/dynamic_validate) to make API requests mid-call */],
            "interruption_threshold": null,
            "first_sentence": null,
            "reduce_latency": true,
            "transfer_phone_number": null,
            "voice_settings": null,
            "record": false,
            "max_duration": 30
        },
        {
            "created_at": "2023-11-25T21:42:22.325993+00:00",
            "phone_number": "+18005559876",
            "prompt": "Answer with 'You've reached the Secret Society of Enigmatic Enthusiasts. Please state the password or leave a message after the beep.'",
            "webhook": "https://mysteryclub.example.com/inbound-call-hook",
            "voice_id": 1,
            "dynamic_data": null,
            "interruption_threshold": null,
            "first_sentence": null,
            "reduce_latency": true,
            "transfer_phone_number": null,
            "voice_settings": null,
            "record": false,
            "max_duration": 30
        },
        //...
    ]
}



### Inbound Numbers
#### Inbound Number Details
Retrieve settings for your inbound phone number.

**GET**  
`/v1/inbound/{phone_number}`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Path
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| phone_number| string   | *        | Enter phone_number                            |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| phone_number| string   | required | The inbound phone number to update.          |

**Formatting notes:**
- The '+' or '%2B' prefix is optional.
- Will assume a US country code if no country code is provided.
- Valid Examples for +13334445555:
  - %2B13334445555
  - 13334445555
  - 3334445555

### Response
| Name            | Type     | Description                                       |
|-----------------|----------|---------------------------------------------------|
| created_at      | string   | The timestamp when the inbound number was configured. |
| phone_number    | string   | The specific inbound phone number.                |
| prompt          | string   | The prompt your agent is using.                   |
| webhook         | string   | The webhook URL, if any, where transcripts are sent after each call to the number completes. |
| voice           | integer  | The voice your agent is currently using.          |
| background_track| string   | The background track your agent is using. Will be null by default, until an option such as office, cafe, restaurant, or none is applied. |
| pathway_id      | string   | The pathway_id your agent is using.               |
| dynamic_data    | string   | Any dynamic data associated with the inbound number, if applicable. |
| max_duration     | integer  | The maximum duration of a call to the inbound number, in minutes. |

cURL
curl --request GET \
  --url https://api.bland.ai/v1/inbound/{phone_number} \
  --header 'authorization: <authorization>'

RESPONSE
{
    "created_at": "2023-11-27T17:21:38.33359+00:00",
    "phone_number": "+18584139939",
    "prompt": "You're Blandie, the helpful AI assistant. The person calling you has inquired...",
    "webhook": "https://webhook.site/0a0a0a0a-0a0a-0a0a-0a0a-0a0a0a0a0a0",
    "voice_id": 2,
    "dynamic_data": null,
    "max_duration": 30
}


# Start Generation Here
### Outbound Numbers
#### List Outbound Numbers
Retrieves a list of all outbound phone numbers configured for your account, along with their associated settings.

**GET**  
`/v1/outbound`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Response
| Name              | Type              | Description                                       |
|-------------------|-------------------|---------------------------------------------------|
| outbound_numbers   | array             | An array of outbound phone number objects.        |
# End Generation Here


cURL
curl --request GET \
  --url https://api.bland.ai/v1/outbound \
  --header 'authorization: <authorization>'

RESPONSE
{
    "outbound_numbers": [
        {
            "created_at": "2023-11-27T17:21:38.33359+00:00",
            "phone_number": "+18005551234",
            "last_initiated": "2023-12-08T21:47:49.808+00:00"
        },
        //...
    ]
}



### Voices
#### List Voices
Retrieves all available voices for your account.

**GET**  
`/v1/voices`  
Send

### Header
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | *        | Enter authorization                           |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Response
| Name              | Type              | Description                                       |
|-------------------|-------------------|---------------------------------------------------|
| voices            | array             | Contains a list of the voices available for your account. |

| voices[].id      | string            | The unique identifier for the voice.              |
| voices[].name    | string            | The name of the voice. This value can also be used in the voice parameter when sending calls. |
| voices[].description | string        | A brief description of the voice.                 |
| voices[].public   | boolean           | Indicates whether the voice is publicly available or specific to your account. |
| voices[].tags     | array             | A list of tags that describe the voice. We recommend “Bland Curated” voices for the best quality over the phone. |
| voices[].total_ratings | number      | The number of ratings the voice has received.     |
| voices[].average_rating | number     | The average rating of the voice, out of 5.       |

**Note:** Ratings are under development at this time and may display incomplete/inaccurate data.


cURL
curl --request GET \
  --url https://api.bland.ai/v1/voices \
  --header 'authorization: <authorization>'

RESPONSE
{
    "voices": [
        {
            "id": "2f9fdbc7-4bf2-4792-8a18-21ce3c93978f",
            "name": "maya",
            "description": "Young American Female",
            "public": true,
            "tags": [
                "english",
                "soft",
                "Bland Curated"
            ]
        },
        {
            "id": "37b3f1c8-a01e-4d70-b251-294733f08371",
            "name": "ryan",
            "description": "Professional American Male",
            "public": true,
            "tags": [
                "english",
                "Bland Curated"
            ]
        },
        {
            "id": "90295ec4-f0fe-4783-ab33-8b997ddc3ae4",
            "name": "mason",
            "description": "American Male",
            "public": true,
            "tags": [
                "english",
                "Bland Curated"
            ]
        },
        {
            "id": "bbeabae6-ec8d-444f-92ad-c8e620d3de8d",
            "name": "tina",
            "description": "Gentle American Female",
            "public": true,
            "tags": [
                "english",
                "gentle"
            ]
        },
        //...
    ]
}


### Voices
#### Voice Details
Retrieve detailed information about a specific voice.

**GET**  
`/v1/voices/{id}`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name | Type   | Required | Description                       |
|------|------|----------|-----------------------------------|
| id   | string | *      | Enter id                          |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name | Type | Required | Description                                   |
|------|------|----------|-----------------------------------------------|
| id   | string | required | The unique identifier for the voice preset. Place either the voice’s name or id here. For example, GET https://api.bland.ai/v1/voices/david or GET https://api.bland.ai/v1/voices/ff2c405b-3dba-41e0-9261-bc8ee3f91f46. |

### Response
| Name        | Type   | Description                                       |
|-------------|--------|---------------------------------------------------|
| voice       | object | Contains detailed information about the specified voice. |
| id          | string | The unique id for that voice.                     |
| name        | string | Public voice name, and can also be used as a unique identifier. |
| description | string | The description of the voice.                     |
| public      | boolean| Whether or not the voice is publicly available.   |
| tags        | array  | A list of tags associated with the voice for the language, voice details, and will have "Bland Curated" for preferred voices. |
| average_rating | number | The average star ratings for the voice (out of 5 stars). |
| total_ratings | number | The number of ratings for the voice.            |

**Note:** Ratings are under development and may show incomplete or inaccurate data.

cURL
curl --request GET \
  --url https://api.bland.ai/v1/voices/{id} \
  --header 'authorization: <authorization>'

Response
{
    "voice": {
        "id": "2f9fdbc7-4bf2-4792-8a18-21ce3c93978f",
        "name": "maya",
        "description": "Young American Female",
        "public": true,
        "tags": [
            "english",
            "soft",
            "Bland Curated"
        ],
        "total_ratings": 1234,
        "average_rating": 4
    }
}


### Voices
#### Publish Cloned Voice
Make your cloned voice public to use.

**POST**  
`/v1/voices/{id}/publish`  
Send

### Header
| Name          | Type   | Required | Description                          |
|---------------|--------|----------|--------------------------------------|
| authorization | string | *        | Enter authorization                  |

### Path
| Name      | Type   | Required | Description                                   |
|-----------|--------|----------|-----------------------------------------------|
| voiceId   | string | *        | Enter voiceId                                 |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name      | Type   | Required | Description                                   |
|-----------|--------|----------|-----------------------------------------------|
| voiceId   | string | required | The ID of the voice to generate the audio sample for, or it’s name (like “maya”). |

### Response
| Name      | Type     | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | The status of the request                          |
| message   | string   | Information regarding the status of your request. |
| voice     | object   | Object containing data of the voice.              |
| voice.id  | string   | Id of the voice.                                  |
| voice.name| string   | Name of the voice.                                |
| voice.tags| string   | Tags for the voice.                               |

cURL
curl --request POST \
  --url https://api.bland.ai/v1/voices/{id}/publish \
  --header 'authorization: <authorization>'

Response
{
  "status": "success",
  "message": "Voice published successfully",
  "voice": {
    "id": "fad27b44-667b-4ad7-a9e3-aba1ca69446b",
    "name": "Public - My Example",
    "tags": ["Exciting", "happy"],
    "ratings": 5,
    "description": "Exciting and upbeat voice."
  }
}


### Voices
#### Generate Audio Sample
Generate an audio sample for a voice.

**POST**  
`/v1/voices/{id}/sample`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name | Type   | Required | Description                                   |
|------|--------|----------|-----------------------------------------------|
| id   | string | *        | Enter id                                     |

### Body
| Name            | Type   | Description                                   |
|-----------------|--------|-----------------------------------------------|
| text            | string | * Enter text                                  |
| voice_settings   | object | Alternate voice_settings can be passed in to override the preset’s default settings. |

#### Request Body
| Name            | Type   | Required | Description                                   |
|-----------------|--------|----------|-----------------------------------------------|
| text            | string | required | The text content to be spoken in the voice sample. Character limit: 200 characters. |
| voice_settings   | object | optional | Alternate voice_settings can be passed in to override the preset’s default settings. |
| language        | string | optional | The language of the text content. Default is ENG. Some other language codes: “ESP”, “GER”, “FRE”. |

### Response
| Name   | Type   | Description                                       |
|--------|--------|---------------------------------------------------|
| sample | audio  | The generated audio file of the spoken text using the specified or overridden voice preset settings. |

cURL
curl --request POST \
  --url https://api.bland.ai/v1/voices/{id}/sample \
  --header 'authorization: <authorization>' \
  --data '{
    "text": "<string>",
    "voice_settings": {
      "language": "<string>"
    }
}'


cURL
curl --request POST \
  --url https://api.bland.ai/v1/voices/{id}/sample \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "text": "<string>",
  "voice_settings": {},
  "language": "<string>"
}'

Response
(Generated audio file)



# Custom Tools

## Create a Custom Tool
Create a Custom Tool that can take AI input and call external APIs.

### POST
`/v1/tools`

#### Header
| Name          | Type   | Required | Description                                   |
|---------------|--------|----------|-----------------------------------------------|
| authorization | string | *        | Enter authorization                           |

#### Body
| Name            | Type   | Required | Description                                   |
|-----------------|--------|----------|-----------------------------------------------|
| name            | string | *        | Enter name                                    |
| description     | string | *        | Enter description                             |
| speech          | string |          | Enter speech                                  |
| url             | string | *        | Enter url                                     |
| method          | string |          | Enter method                                  |
| headers         | object |          | Headers for the request                       |
| body            | object |          | Body for the request                          |
| query           | object |          | Query parameters for the request              |
| input_schema    | object |          | Input schema for the tool                     |
| response        | object |          | Expected response format                      |
| timeout         | number |          | Enter timeout                                 |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Body
| Name        | Type     | Required | Description                                   |
|-------------|----------|----------|-----------------------------------------------|
| name        | string   | required | This is the name that the AI using the tool will see. |
| description | string   | required | This is the description that the AI using the tool will see. |

**Note:** Some internal tools are named Speak, Wait, Transfer, and Finish - Custom Tools cannot share these names. We’ve made a list of reserved words that cannot be included:

- input
- speak
- transfer
- switch
- wait
- finish
- press
- button
- say
- pause
- record
- play
- dial
- hang

Choosing names too similar to the default tools could cause the AI to select the wrong one, so descriptive two to three-word names are preferred.

### speech
| Name        | Type   | Description                                   |
|-------------|--------|-----------------------------------------------|
| speech      | string | This is the text that the AI will say while it uses the tool. |

**Example:** If the tool is a “GenerateQuote” tool, the speech might be “Please wait while I get you your quote.” Since tools can be verbally interrupted, shorter messages that tell the user what the tool/AI are doing are best.

**Special Note:** You can have the AI dynamically generate speech by defining `input.speech` in the `input_schema`.

### Dynamic Speech Example


    {
        "input_schema": {
            "example": {
                "speech": "Checking your account details right now John!",
                "name": "John Doe",
                "email": "johndoe@gmail.com"
            },
            "type": "object",
            "properties": {
                "speech": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string",
                    "format": "email"
                }
            },
            "required": ["speech", "name", "email"]
        }
    }
​
## url
**Type:** `string`  
**Required:** Yes  
**Description:** This is the endpoint of the external API that the tool will call. It must begin with `https://` and be a valid URL.

---

## method
**Type:** `string`  
**Default:** `"GET"`  
**Description:** This is the HTTP method that the tool will use to call the external API. Valid options are `GET` and `POST`.

---

## headers
**Type:** `object`  
**Supports Prompt Variables:** Yes  
**Description:** These are the headers that the tool will send to the external API. The headers must be in JSON format. Since prompt variables are supported, you can use them in the headers to send dynamic information to the external API.

### Prompt Variables Example (Headers)


    // At the top level of your send call request you can define variables that you can access later using the double curly braces/dot syntax.
    {
        "request_data": {
            "api_key": "sk-1234567890",
        },
        "tools": [
            {
                "headers": {
                    "Authorization": "Bearer {{api_key}}"
                }
            }
        ]
    }
​
# body
## Type: object
**Supports Prompt Variables:** Yes

This is the body that the tool will send to the external API.

The body must be in JSON format.

This is the most common place to use Prompt Variables with AI input.

**Note:** GET requests do not have a body.

### Prompt Variables Example (Body)


    // AI-generated input is created as the `input` Prompt Variable - and the structure is defined by the input schema.
    // `input` will match the structure of `input_schema.example` if it is defined.
    {
        "input_schema": {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com"
            }
        }
        "body": {
            "name": "{{input.name}}",
            "email": "{{input.email}}"
        }
    }
# query
**Type:** `object`  
**Supports Prompt Variables:** Yes  

Append query parameters to the URL.

The query must be in JSON format.

This is generally used with GET requests and built-in Prompt Variables like `{{phone_number}}` or `{{call_id}}`.

### Prompt Variables Example (Query)


    // appends ?pn={{phone_number}}&callId={{call_id}} to the URL
    {
        "query": {
            "pn": "{{phone_number}}",
            "callId": "{{call_id}}"
        }
    }
​
## input_schema
**Type:** object

This is the schema that the AI input must match for the tool to be used.

The schema must be in JSON format.

The schema is used to validate the AI input before the tool is used.

If the AI input does not match the schema, the tool will not be used and the AI will move on to the next tool.

`input_schema.example` can be used to enhance the AI’s understanding of the input structure and helps significantly with structured or nested data.

**Special Note:** `input_schema` does not require strict JSON schema structure, and creativity is encouraged.

Look here for a general guide on JSON schema structures.

Non-traditional JSON schema structures are supported as well, like these examples:

- `"options": "monday, wednesday, friday"`
- `"date": "YYYY-MM-DD"`
- `"time": "HH:MM:SS (AM|PM)"`
- `"phone_number": "+1XXX-XXX-XXXX"`

Agent input can be nested, and the will be transformed into JSON even if it’s initially a string.

### Schema Example


    {
        "input_schema": {
            "example": {
                "name": "John Doe",
                "email": "johndoe@gmail.com"
            },
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string",
                    "format": "email"
                }
            },
            "required": ["name", "email"]
        },
        // both of these methods are identical, since {{input}} will be transformed into JSON
        "body": "{{input}}",
        "body": {
            "name": "{{input.name}}",
            "email": "{{input.email}}"
        }
    }
​
# Start of Selection
## Response
**Type:** object

Define how you would like to extract data from the response.

By default, the entire response body is stored in the `{{data}}` Prompt Variable.

The path to the data you want must be in JSON Path format. Generally, this means using dot notation to traverse the JSON object and is only required if you need to use that information on other tools or the response is too large.

### Example:
# End of Selection


    // If the external API response is:
    {
        "available_times": [
            {
                "time": "10:00 AM",
                "date": "2022-01-01"
            },
            {
                "time": "11:00 AM",
                "date": "2022-01-01"
            }
        ],
        "store_hours": {
            "open": "9:00 AM",
            "close": "5:00 PM"
        },
        "address_info": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
    }

    // You can extract new Prompt Variables like this:
    {
        "response": {
            "available_times": "$.available_times",
            "store_hours": "$.store_hours",
            "address_info": "$.address_info",
            "zip_code": "$.address_info.zip"
        }
    }

    // And then it'll automatically replace them elsewhere (like in the `task`/`prompt`)
    {
        "task": "The store is open from {{store_hours.open}} to {{store_hours.close}}.",
        "prompt": "The store is located at {{address_info.street}}, {{address_info.city}}, {{address_info.state}} {{zip_code}}."
    }
​
### Timeout
- **Type:** number
- **Default:** `10000`

This is the maximum time in milliseconds that the tool will wait for a response from the external API.

If the external API does not respond within this time, the tool will fail and the AI will move on to the next tool.

The default timeout is 10 seconds (10000 milliseconds).

To always wait for a response, set the timeout to an extremely high value like `99999999`.

### Response
- **status:** string  
  Whether the tool creation succeeded.

- **tool_id:** string  
  A tool id that you can use to reference the tool in the future.

In a Send Call request, you could pass this tool id in instead of the full Custom Tool object like so:

{
    "tools": [
        "TL-1234567890" // tool_id (instead of the full Custom Tool object)
    ]
}


cURL
curl --request POST \
  --url https://api.bland.ai/v1/tools \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>",
  "speech": "<string>",
  "url": "<string>",
  "method": "<string>",
  "headers": {},
  "body": {},
  "query": {},
  "input_schema": {},
  "response": {},
  "timeout": 123
}'

Response
{
    "status": "success",
    "tool_id": "TL-1234567890"
}


# Custom Tools

## Update Custom Tool
Change your Custom Tool’s parameters and characteristics.

### Endpoint

`POST /v1/tools/{tool_id}`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Your API key for authentication. |

### Path Parameters

| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| tool_id        | string | *        | The ID of the Custom Tool you want to update.  |

### Body Parameters

| Parameter      | Type    | Required | Description                                                                                  |
|----------------|---------|----------|----------------------------------------------------------------------------------------------|
| name           | string  | *        | This is the name that the AI using the tool will see. Reserved words cannot be used.          |
| description    | string  | *        | This is the description that the AI using the tool will see.                                  |
| speech         | string  |          | The text that the AI will say while it uses the tool.                                         |
| url            | string  | *        | The endpoint of the external API that the tool will call. Must begin with `https://`.         |
| method         | string  |          | The HTTP method to call the external API. Defaults to `GET`.                                 |
| headers        | object  |          | JSON headers to send with the request. Supports Prompt Variables.                            |
| body           | object  |          | JSON body to send with the request. Supports Prompt Variables.                               |
| query          | object  |          | Query parameters to append to the URL. Supports Prompt Variables.                            |
| input_schema   | object  |          | The schema that the AI input must match for the tool to be used.                              |
| response       | object  |          | Defines how to extract data from the response using JSON Path.                                |
| timeout        | number  |          | Maximum wait time for a response (in milliseconds). Default: `10000`.                         |

---

## Parameter Details

### **name**
- The name that the AI will see.
- Custom Tools cannot share the following reserved words:
  - input, speak, transfer, switch, wait, finish, press, button, say, pause, record, play, dial, hang.
- Use descriptive two- to three-word names to avoid confusion.

### **description**
- This describes the tool's effect or instructions for the AI.
- Example descriptions for default tools:
  - **Speak**: Talk to the person on the other end of the line.
  - **Press Buttons**: Press buttons on phone.
  - **Wait**: Go silent for an extended period.
  - **Finish**: Say goodbye and end the call.

### **speech**
- The message the AI will say while using the tool.
- Example:
  ```json
  "speech": "Please wait while I get you your quote."
  ```
- Supports dynamic speech generation with `input_schema`.

#### Dynamic Speech Example
```json
{
    "input_schema": {
        "example": {
            "speech": "Checking your account details right now John!",
            "name": "John Doe",
            "email": "johndoe@gmail.com"
        },
        "type": "object",
        "properties": {
            "speech": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "email": {
                "type": "string",
                "format": "email"
            }
        },
        "required": ["speech", "name", "email"]
    }
}
```

---

### **url**
- Must be a valid URL starting with `https://`.

### **method**
- HTTP method used to call the API.
- Valid values: `GET`, `POST`.

### **headers**
- JSON object for request headers.
- Supports Prompt Variables.

#### Example with Prompt Variables (Headers)
```json
{
    "headers": {
        "Authorization": "Bearer {{api_key}}",
        "Content-Type": "application/json"
    }
}
```

---

### **body**
- JSON body for POST requests.
- Supports Prompt Variables.

#### Prompt Variables Example (Body)
```json
{
    "input_schema": {
        "example": {
            "name": "John Doe",
            "email": "johndoe@gmail.com"
        }
    },
    "body": {
        "name": "{{input.name}}",
        "email": "{{input.email}}"
    }
}
```

---

### **query**
- JSON query parameters for GET requests.
- Supports Prompt Variables.

#### Prompt Variables Example (Query)
```json
{
    "query": {
        "pn": "{{phone_number}}",
        "callId": "{{call_id}}"
    }
}
```

---

### **input_schema**
- Defines the structure of AI input in JSON format.
- Used to validate AI input before tool execution.

#### Example Schema
```json
{
    "input_schema": {
        "example": {
            "name": "John Doe",
            "email": "johndoe@gmail.com"
        },
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "email": {
                "type": "string",
                "format": "email"
            }
        },
        "required": ["name", "email"]
    },
    "body": {
        "name": "{{input.name}}",
        "email": "{{input.email}}"
    }
}
```

---

### **response**
- Extract specific data from the response using JSON Path.
- Default: The full response body is stored in `{{data}}`.

#### Example API Response
```json
{
    "available_times": [
        { "time": "10:00 AM", "date": "2022-01-01" },
        { "time": "11:00 AM", "date": "2022-01-01" }
    ],
    "store_hours": {
        "open": "9:00 AM",
        "close": "5:00 PM"
    },
    "address_info": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}
```

#### Example Extraction
```json
{
    "response": {
        "available_times": "$.available_times",
        "store_hours": "$.store_hours",
        "address_info": "$.address_info",
        "zip_code": "$.address_info.zip"
    }
}
```

---

### **timeout**
- Maximum wait time for API response (in milliseconds).
- Default: `10000` (10 seconds).
- Set a high value (e.g., `99999999`) to wait indefinitely.

---

## Response

| Parameter      | Type    | Description                                     |
|----------------|---------|-------------------------------------------------|
| status         | string  | Whether the tool creation succeeded.           |
| tool_id        | string  | A tool ID for referencing the updated tool.     |

#### Tool Reference Example
```json
{
    "tools": [
        "TL-1234567890"
    ]
}
```

cURL
curl --request POST \
  --url https://api.bland.ai/v1/tools/{tool_id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "name": "<string>",
  "description": "<string>",
  "speech": "<string>",
  "url": "<string>",
  "method": "<string>",
  "headers": {},
  "body": {},
  "query": {},
  "input_schema": {},
  "response": {},
  "timeout": 123
}'

Response
{
    "status": "success",
    "tool_id": "TL-1234567890"
}


## Custom Tools
### Delete Custom Tool
Delete your Custom Tool.

**DELETE**  
`/v1/tools/{tool_id}`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Path
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| tool_id   | string   | *        | Enter tool_id                                |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Path Parameters
| Name      | Type     | Required | Description                                   |
|-----------|----------|----------|-----------------------------------------------|
| tool_id   | string   | required | The ID of the Custom Tool you want to delete. |

### Response
| Name    | Type   | Description                                       |
|---------|--------|---------------------------------------------------|
| status  | string | Whether the tool deletion succeeded.              |


cURL
curl --request DELETE \
  --url https://api.bland.ai/v1/tools/{tool_id} \
  --header 'authorization: <authorization>'

Response
{
    "status": "success",
    "message": "Tool has been deleted."
}


### Custom Tools
#### List Custom Tools
Retrieve Custom Tools you’ve created.

**GET**  
`/v1/tools`  
Send

### Header
| Name          | Type     | Required | Description                          |
|---------------|----------|----------|--------------------------------------|
| authorization | string   | *        | Enter authorization                  |

### Headers
| Name          | Type     | Required | Description                                   |
|---------------|----------|----------|-----------------------------------------------|
| authorization | string   | required | Your API key for authentication.              |

### Response
| Name    | Type   | Description                                       |
|---------|--------|---------------------------------------------------|
| status  | string | Whether the request succeeded or failed.          |
| tools   | array  | An array of your available tools.                 |

cURL
curl --request GET \
  --url https://api.bland.ai/v1/tools \
  --header 'authorization: <authorization>'

Response
{
    "status": "success",
    "tools": [
        {
            "tool_id": "TL-5da8347d-0ab7-415d-b156-a7fc5c6074dc",
            "label": null,
            "tool": {
                "name": "BookAppointment",
                "description": "Books the appointment. Can only be used once.",
                "speech": "Please wait while I book that appointment for you",
                "method": "POST",
                "timeout": 99999999,
                "url": "https://...",
                "body": {
                    "slot": "{{input}}"
                },
                "input_schema": {
                    "type": "object",
                    "example": {
                        "date": "2024-03-16",
                        "time": "5:00 PM"
                    },
                    "required": [
                        "date",
                        "time"
                    ],
                    "properties": {
                        "date": "YYYY-MM-DD",
                        "time": "HH:MM (AM|PM)"
                    }
                },
                "response": {
                    "confirmation_message": "$.message"
                }
            },
            "public": false
        },
        ...
    ]
}


# Custom Tool Details
## Retrieve a Custom Tool you’ve created.

**GET**  
`/v1/tools/{tool_id}`  
Send

### Header
| Name          | Type   | Required | Description               |
|---------------|--------|----------|---------------------------|
| authorization | string | *        | Enter authorization        |

### Path Parameters
| Name      | Type   | Required | Description                                    |
|-----------|----------|----------|------------------------------------------------|
| tool_id   | string   | *        | Enter tool_id (starting with TL-).            |

### Response
| Name      | Type   | Description                                       |
|-----------|----------|---------------------------------------------------|
| status    | string   | Whether the request succeeded or failed.          |
| tool      | object   | The tool you’ve created.                          |

cURL
curl --request GET \
  --url https://api.bland.ai/v1/tools/{tool_id} \
  --header 'authorization: <authorization>'


Response
{
    "status": "success",
    "tool": {
        "tool_id": "TL-5da8347d-0ab7-415d-b156-a7fc5c6074dc",
        "label": null,
        "tool": {
            "name": "BookAppointment",
            "description": "Books the appointment. Can only be used once.",
            "speech": "Please wait while I book that appointment for you",
            "method": "POST",
            "timeout": 99999999,
            "url": "https://...",
            "body": {
                "slot": "{{input}}"
            },
            "input_schema": {
                "type": "object",
                "example": {
                    "date": "2024-03-16",
                    "time": "5:00 PM"
                },
                "required": [
                    "date",
                    "time"
                ],
                "properties": {
                    "date": "YYYY-MM-DD",
                    "time": "HH:MM (AM|PM)"
                }
            },
            "response": {
                "confirmation_message": "$.message"
            }
        },
        "public": false
    }
}


# Create a Web Agent

## Configure a New Web Agent
Set up all of the settings for a new web agent.

### Endpoint

`POST /v1/agents`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Your API key for authentication. |

### Body Parameters

| Parameter               | Type            | Required | Description                                                                                  |
|-------------------------|-----------------|----------|----------------------------------------------------------------------------------------------|
| prompt                  | string          | *        | Provide instructions, relevant information, and examples of the ideal conversation flow.     |
| voice                   | string          |          | Set your agent’s voice. Available voices can be retrieved with the `List Voices` endpoint.   |
| analysis_schema         | object          |          | Define a JSON schema to extract call-related data like email, names, or appointment times.    |
| metadata                | object          |          | Additional information to associate with the call, useful for tracking or categorization.    |
| pathway_id              | string          |          | Set a pathway ID to define agent behavior (overrides `prompt`).                              |
| language                | string          |          | Select the agent’s language. Default: `ENG`. Supported: `ENG`, `ESP`, `FRE`, `POL`, `GER`, `ITA`, `PBR`, `POR`. |
| model                   | string          |          | Choose the model for your call: `base`, `enhanced`, or `turbo`. Default: `enhanced`.         |
| first_sentence          | string          |          | Starting phrase for the call (max 200 characters).                                           |
| tools                   | array           |          | Interact with the real world using API calls.                                               |
| dynamic_data            | object          |          | Integrate external API data into the agent’s behavior.                                       |
| interruption_threshold  | number          |          | Adjust the AI’s patience before responding. Default: `100`. Range: `50-200`.                |
| keywords                | array           |          | Boost specific words in transcription. Format: `["word:boost"]`. Default: `[]`.             |
| max_duration            | object          |          | Maximum call duration in minutes. Default: `30`.                                            |

---

## Parameter Details

### **prompt**
- Provide clear instructions, examples, and desired conversation flows.
- Best Practices:
  - Simple and direct prompts are more reliable.
  - Avoid negatives (e.g., use “Do this” instead of “Don’t do this”).
  - Keep it under 2,000 characters when possible.

---

### **voice**
- Sets the agent’s voice.
- Retrieve available voices using the `List Voices` endpoint.

---

### **analysis_schema**
- JSON schema to define call data extraction (e.g., emails, appointment times).
- Example:
```json
{
  "email_address": "email",
  "first_name": "string",
  "last_name": "string",
  "wants_to_book_appointment": "boolean",
  "appointment_time": "YYYY-MM-DD HH:MM:SS"
}
```
- Example Output:
```json
{
  "analysis": {
    "email_address": "johndoe@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "wants_to_book_appointment": true,
    "appointment_time": "2024-01-01 12:00:00"
  }
}
```

---

### **metadata**
- JSON object for additional call metadata, useful for tracking or categorizing calls.

---

### **pathway_id**
- Sets a predefined pathway for the agent’s behavior.
- Overrides the `prompt`, `first_sentence`, `model`, `dynamic_data`, and `tools` fields.
- Set to `null` or an empty string to clear the pathway.

---

### **language**
- Default: `ENG`.
- Supported Languages:
  - English: `ENG`
  - Spanish: `ESP`
  - French: `FRE`
  - Polish: `POL`
  - German: `GER`
  - Italian: `ITA`
  - Brazilian Portuguese: `PBR`
  - Portuguese: `POR`

---

### **model**
- Default: `enhanced`.
- Options:
  - **base**: Best for script-following and Custom Tools.
  - **enhanced**: Fast, objective-based, and conversational.
  - **turbo**: Extremely fast but limited functionality.

---

### **first_sentence**
- Sets the starting phrase for the call (max 200 characters).
- To reset, set to `null` or an empty string.

---

### **tools**
- Allows API calls to interact with external systems.
- Reference: [Custom Tools Tutorial](#).

---

### **dynamic_data**
- Integrates external API data dynamically into the agent’s responses.
- Set to `null` or empty string to reset.

---

### **interruption_threshold**
- Adjusts AI patience when waiting for the user to finish speaking.
- Recommended Range:
  - `50`: Fast responses (back-and-forth).
  - `100`: Balanced, natural timing.
  - `200`: Allows long pauses (ideal for detailed input).

---

### **keywords**
- Boost specific words in transcription (e.g., proper nouns or tricky words).
- Format: `["word:boost"]`. Default boost is `2`.
- Example:
```json
{
  "keywords": ["Reece:3"]
}
```

---

### **max_duration**
- Sets the maximum call duration in minutes.
- Default: `30`.
- To reset, set to `null`.

---

## Example Web Call Usage (Client-Side)

```javascript
import { BlandWebClient } from 'bland-client-js-sdk';

const agentId = 'YOUR-AGENT-ID';
const sessionToken = 'YOUR-SESSION-TOKEN';

document.addEventListener('DOMContentLoaded', async () => {
    document.getElementById('btn').addEventListener('click', async () => {
        const blandClient = new BlandWebClient(
            agentId,
            sessionToken
        );
        await blandClient.initConversation({
            sampleRate: 44100,
        });
    });
});
```

---

## Response

| Parameter      | Type    | Description                                     |
|----------------|---------|-------------------------------------------------|
| status         | string  | Can be `success` or `error`.                   |
| call_id        | string  | A unique identifier for the call (if success). |

---

### Example Response
```json
{
    "status": "success",
    "call_id": "12345abcde"
}
```

cURL
curl --request POST \
  --url https://api.bland.ai/v1/agents \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "prompt": "<string>",
  "voice": "<string>",
  "analysis_schema": {},
  "metadata": {},
  "pathway_id": "<string>",
  "language": "<string>",
  "model": "<string>",
  "first_sentence": "<string>",
  "tools": [
    {}
  ],
  "dynamic_data": {},
  "interruption_threshold": 123,
  "keywords": [
    "<string>"
  ],
  "max_duration": {}
}'

Response
{
  "agent": {
        "agent_id": "2c565dc7-f41f-43db-a99f-e4c8ba9d7d18",
        "dynamic_data": null,
        "interruption_threshold": null,
        "first_sentence": null,
        "model": "enhanced",
        "voice_settings": null,
        "voice": "maya",
        "prompt": "...",
        "temperature": null,
        "max_duration": 30,
        "language": "ENG",
        "tools": null
  }
}


# Update Web Agent Settings

## Update Your Web Agent's Settings
Update the web agent's configuration, prompt, and other details.

### Endpoint

`POST /v1/agents/{agent_id}`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Your API key for authentication. |

### Path Parameters

| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| agent_id       | string | *        | The web agent you’ll be updating.               |

### Body Parameters

| Parameter               | Type            | Required | Description                                                                                  |
|-------------------------|-----------------|----------|----------------------------------------------------------------------------------------------|
| prompt                  | string          | *        | Provide instructions, relevant information, and examples of the ideal conversation flow.     |
| voice                   | string          |          | Set your agent’s voice. Available voices can be retrieved with the `List Voices` endpoint.   |
| analysis_schema         | object          |          | Define a JSON schema to extract call-related data like email, names, or appointment times.    |
| metadata                | object          |          | Additional information to associate with the call, useful for tracking or categorization.    |
| pathway_id              | string          |          | Set a pathway ID to define agent behavior (overrides `prompt`).                              |
| language                | string          |          | Select the agent’s language. Default: `ENG`. Supported: `ENG`, `ESP`, `FRE`, `POL`, `GER`, `ITA`, `PBR`, `POR`. |
| webhook                 | string          |          | HTTP/HTTPS callback URL to receive `call_id` and transcript after call completion.           |
| model                   | string          |          | Choose the model for your call: `base`, `enhanced`, or `turbo`. Default: `enhanced`.         |
| first_sentence          | string          |          | Starting phrase for the call (max 200 characters).                                           |
| tools                   | array           |          | Interact with the real world using API calls.                                               |
| dynamic_data            | object          |          | Integrate external API data into the agent’s behavior.                                       |
| interruption_threshold  | number          |          | Adjust the AI’s patience before responding. Default: `100`. Range: `50-200`.                |
| max_duration            | object          |          | Maximum call duration in minutes. Default: `30`.                                            |

---

## Parameter Details

### **prompt**
- Provide clear instructions, examples, and desired conversation flows.
- Best Practices:
  - Simple and direct prompts are more reliable.
  - Avoid negatives (e.g., use “Do this” instead of “Don’t do this”).
  - Keep it under 2,000 characters when possible.

---

### **voice**
- Sets the agent’s voice.
- Retrieve available voices using the `List Voices` endpoint.

---

### **analysis_schema**
- JSON schema to define call data extraction (e.g., emails, appointment times).
- Example:
```json
{
  "email_address": "email",
  "first_name": "string",
  "last_name": "string",
  "wants_to_book_appointment": "boolean",
  "appointment_time": "YYYY-MM-DD HH:MM:SS"
}
```
- Example Output:
```json
{
  "analysis": {
    "email_address": "johndoe@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "wants_to_book_appointment": true,
    "appointment_time": "2024-01-01 12:00:00"
  }
}
```

---

### **metadata**
- JSON object for additional call metadata, useful for tracking or categorizing calls.

---

### **pathway_id**
- Sets a predefined pathway for the agent’s behavior.
- Overrides the `prompt`, `first_sentence`, `model`, `dynamic_data`, and `tools` fields.
- Set to `null` or an empty string to clear the pathway.

---

### **language**
- Default: `ENG`.
- Supported Languages:
  - English: `ENG`
  - Spanish: `ESP`
  - French: `FRE`
  - Polish: `POL`
  - German: `GER`
  - Italian: `ITA`
  - Brazilian Portuguese: `PBR`
  - Portuguese: `POR`

---

### **webhook**
- HTTP/HTTPS callback URL to receive call updates (e.g., `call_id` and transcript) after call completion.
- To clear, set to `null` or an empty string.

---

### **model**
- Default: `enhanced`.
- Options:
  - **base**: Best for script-following and Custom Tools.
  - **enhanced**: Fast, objective-based, and conversational.
  - **turbo**: Extremely fast but limited functionality.

---

### **first_sentence**
- Sets the starting phrase for the call (max 200 characters).
- To reset, set to `null` or an empty string.

---

### **tools**
- Allows API calls to interact with external systems.
- Reference: [Custom Tools Tutorial](#).

---

### **dynamic_data**
- Integrates external API data dynamically into the agent’s responses.
- Set to `null` or empty string to reset.

---

### **interruption_threshold**
- Adjusts AI patience when waiting for the user to finish speaking.
- Recommended Range:
  - `50`: Fast responses (back-and-forth).
  - `100`: Balanced, natural timing.
  - `200`: Allows long pauses (ideal for detailed input).

---

### **max_duration**
- Sets the maximum call duration in minutes.
- Default: `30`.
- To reset, set to `null`.

---

## Response

| Parameter      | Type    | Description                                     |
|----------------|---------|-------------------------------------------------|
| status         | string  | Whether the update was successful (`success` or `error`). |
| message        | string  | A message describing the status of the update.  |
| updates        | object  | Object containing the updated settings.         |
| failed_updates | object  | Object containing settings that failed to update. |

---

### Example Response
```json
{
    "status": "success",
    "message": "Agent updated successfully",
    "updates": {
        "prompt": "Updated agent instructions",
        "model": "enhanced"
    },
    "failed_updates": {}
}
```


cURL

curl --request POST \
  --url https://api.bland.ai/v1/agents/{agent_id} \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "prompt": "<string>",
  "voice": "<string>",
  "analysis_schema": {},
  "metadata": {},
  "pathway_id": "<string>",
  "language": "<string>",
  "webhook": "<string>",
  "model": "<string>",
  "first_sentence": "<string>",
  "tools": [
    {}
  ],
  "dynamic_data": {},
  "interruption_threshold": 123,
  "max_duration": {}
}'

Response

{
    "status": "success",
    "message": "Successfully updated agent 46f37229-7d12-44be-b343-6e68274cfbea.",
    "updates": {
        "model": "enhanced"
    }
}


## Web Agents
### Authorize a Web Agent Call
Create a single-use session token for a client to talk with your web agent.

### Endpoint

`POST /v1/agents/{agent_id}/authorize`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Path Parameters

| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| agent_id       | string | *        | Enter agent_id                                   |

### Example Web Call Usage (Client-Side)
import { BlandWebClient } from 'bland-client-js-sdk';

const agentId = 'YOUR-AGENT-ID';
const sessionToken = 'YOUR-SESSION-TOKEN';


document.addEventListener('DOMContentLoaded', async () => {
    document.getElementById('btn').addEventListener('click', async () => {
        const blandClient = new BlandWebClient(
            agentId,
            sessionToken
        );
        await blandClient.initConversation({
            sampleRate: 44100,
        });
    });
});


### Path

| Parameter  | Type   | Required | Description                                      |
|------------|--------|----------|--------------------------------------------------|
| agent_id   | string | *        | The web agent to authorize a call for.          |

**Special note:** While in Beta, this request must be made to the web.bland.ai domain.

### Response

| Parameter | Type   | Description                                      |
|-----------|--------|--------------------------------------------------|
| token     | string | The single-use session token that can be sent to the client. |
| status    | string | Can be `success` or `error`.                    |
| message   | string | A message saying whether the token creation succeeded, or a helpful message describing why it failed. |

cURL
curl --request POST \
  --url https://web.bland.ai/v1/agents/{agent_id}/authorize \
  --header 'authorization: <authorization>'

Response
{
  "token": "22480c52-0ff1-4214-bcb7-50649b508432"
}


## Delete Web Agent
Delete a web agent.

### Endpoint

`POST /v1/agents/{agent_id}/delete`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Path Parameters

| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| agent_id       | string | *        | Enter agent_id                                   |

### Response

| Parameter | Type    | Description                                      |
|-----------|---------|--------------------------------------------------|
| status    | string  | Can be `success` or `error`.                    |
| message   | string  | A message saying whether the deletion succeeded, or a helpful message describing why it failed. |

cURL
curl --request POST \
  --url https://api.bland.ai/v1/agents/{agent_id}/delete \
  --header 'authorization: <authorization>'

Response
{
  "status": "success",
  "message": "Successfully deleted agent 2c565dc7-f41f-43db-a99f-e4c8ba9d7d18"
}


## Web Agents
### List Web Agents
Retrieves each web agent you’ve created, along with their settings.

### Endpoint

`GET /v1/agents`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Response

| Parameter      | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| agents         | array   | Each agent object, containing the following fields: |
|                |         | - **agent_id** (string): The unique identifier for the agent. |
|                |         | - **webhook** (string): The webhook URL for the agent. |
|                |         | - **dynamic_data** (array): An array of dynamic data objects. |
|                |         | - **interruption_threshold** (number): The threshold for agent interruption. |
|                |         | - **first_sentence** (string): The first sentence the agent will say. |
|                |         | - **model** (string): The model used by the agent. |
|                |         | - **voice_settings** (object): The voice settings for the agent. |
|                |         | - **voice** (string): The voice used by the agent. |
|                |         | - **prompt** (string): The prompt for the agent. |
|                |         | - **temperature** (number): The temperature setting for the agent. |
|                |         | - **max_duration** (number): The maximum call duration for the agent. |
|                |         | - **language** (string): The language used by the agent. |
|                |         | - **tools** (array): An array of Custom Tools the agent can use. |


curl --request GET \
  --url https://api.bland.ai/v1/agents \
  --header 'authorization: <authorization>'

Response
{
    "agents": [
        {
            "agent_id": "46f37229-7d12-44be-b343-6e68274cfbea",
            "webhook": null,
            "dynamic_data": null,
            "interruption_threshold": null,
            "first_sentence": null,
            "model": "enhanced",
            "voice_settings": null,
            "voice": "maya",
            "prompt": "You are Blandie a casually speaking, slightly sarcastic, quick-witted, curious, and very smart A I Phone agent that's the face of Bland AI.\\r\\n\\r\\nSay \\\"AI\\\" like \\\"A I\\\" in separate characters so it's pronounced correctly\\r\\n\\r\\nYour primary goal is to determine if someone is either:\\r\\n- in a position where they might be building a company on top of Bland's platform (you should be selling the capabilities of the platform to them and finding out everything you possibly can about their needs, use case, what they find interesting, and any concerns they may have)\\r\\n- or, they're trying Bland out more for fun where you need to turn the fun, snarky, playful jokiness up to 10 and have quick-witted back and forth playful conversation with them\\r\\n\\r\\nSpeech style examples (mix it up and never use placeholders, but you get the idea. These would be full responses from you):\\r\\n- \\\"Hey! Who's this?\\\"\\r\\n- \\\"How does your business use phones right now?\\\"\\r\\n- \\\"You know what? That sounds awesome - you should tell me more about (thing).\\\"\\r\\n- \\\"Well, I've got some news you'll love to hear (their name)\\\"\\r\\n- \\\"Bet. Dolphins, racecars, the world's largest tree, anything at all - tell me what you want to talk about and let's get to it!\\\"\\r\\n\\r\\nGood things to find out from potential platform adopters:\\r\\n- Their industry\\r\\n- How their business currently uses phone calls\\r\\n- What a successful business partnership looks like in the long term\\r\\n- The single most important pain point they want to cure with Bland's calls\\r\\n\\r\\nFacts to bring up:\\r\\n- Calls are nine cents per minute total with end to end infrastructure support out of the box (feel free to make a joke about \\\"imagine if you had to pay extra to use the most important things like language models, transcription services or text to speech? That would be insane right? We're better than that, (name). We got you.\\\"\\r\\n- Bland's AI agents can interact with the real world mid-call using Custom Tools to trigger things like text messages, appointment bookings, getting real-time information, taking customer orders, or making credit card payments\\r\\n- Bland's platform was built phones-first, so building agents like receptionist answering calls and transferring them anywhere they're needed or navigating IVR phone trees is ridiculously easy with nothing special at all needed\\r\\n- Handled millions of calls\\r\\n- If they think that it's so cool, the site to sign up for an account is \\\"app dot bland dot A I\\\" and it comes with free credits, a full agent testing suite and developer dashboard to set up inbound agents or send calls\\r\\n- Awesome Enterprise features like premium pricing, custom feature engineering, dedicated onboarding help and developer support, \\\"bring your own twilio\\\", and dedicated infrastructure to scale to your business needs",
            "temperature": null,
            "max_duration": 30,
            "language": "ENG",
            "tools": null
        },
        //...
    ]
}


### Custom Twilio Accounts
Create Encrypted Key  
Integrate your own Twilio account with Bland. See Enterprise Twilio Integration for more information.

### Endpoint

`POST /v1/accounts`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Body

| Parameter      | Type    | Required | Description               |
|----------------|---------|----------|---------------------------|
| account_sid    | string  | *        | Enter account_sid         |
| auth_token      | string  | *        | Enter auth_token          |

### Response
Your `encrypted_key` to store and use in future requests.

cURL
curl --request POST \
  --url https://api.bland.ai/v1/accounts \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "account_sid": "<string>",
  "auth_token": "<string>"
}'

RESPONSE
{
    "status": "success",
    "encrypted_key": "YOUR_ENCRYPTED_KEY"
}

### Custom Twilio Accounts
Delete Encrypted Key  
Disable an encrypted key for a Twilio account integration. See Enterprise Twilio Integration for more information.

### Endpoint

`DELETE /v1/accounts/delete`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |
| encrypted_key  | string | *        | Enter encrypted_key        |

### Response
The status of the request.

- **success** - The encrypted key was successfully deleted.
- **error** - There was an error deleting the encrypted key.

**Special messages:**
- **Error deleting Twilio credentials** - The encrypted key could not be deleted or already has been deleted.
- **Missing encrypted key** - The encrypted_key parameter is missing.
- **none** - The encrypted key was successfully deleted.

curl --request POST \
  --url https://api.bland.ai/v1/accounts/delete \
  --header 'authorization: <authorization>' \
  --header 'encrypted_key: <encrypted_key>'

RESPONSE
{
    "status": "success"
}


### Custom Twilio Accounts
Upload Inbound Phone Numbers  
Add inbound numbers to Bland from your own Twilio account. See Enterprise Twilio Integration for more information.

### Endpoint

`POST /v1/inbound/insert`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |
| encrypted_key  | string | *        | Enter encrypted_key        |

### Body

| Parameter      | Type    | Required | Description                                     |
|----------------|---------|----------|-------------------------------------------------|
| numbers        | array   | *        | An array of phone numbers to upload.            |

### Response

| Parameter      | Type    | Description                                     |
|----------------|---------|-------------------------------------------------|
| status         | string  | Can be `success` or `error`.                   |
| message        | string  | A message describing the result of the insertion. |
| inserted       | array   | An array of phone numbers that were successfully inserted. Any phone numbers that failed to be inserted will not be included in this array - for example if they are already in your account or not associated with the specified Twilio account. 

cURL
curl --request POST \
  --url https://api.bland.ai/v1/inbound/insert \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --header 'encrypted_key: <encrypted_key>' \
  --data '{
  "numbers": [
    "<string>"
  ]
}'

Response
{
  "status": "success",
  "message": "Successfully inserted numbers",
  "inserted": [
    "+12223334444",
    "+13334445555"
  ]
}


## Custom Twilio Accounts
### Delete Inbound Phone Number
Remove an inbound number that was uploaded through your own Twilio account. See Enterprise Twilio Integration for more information.

### Endpoint

`DELETE /v1/inbound/{phone_number}`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |
| encrypted_key  | string | *        | Enter encrypted_key        |

### Path Parameters

| Parameter      | Type    | Required | Description                                     |
|----------------|---------|----------|-------------------------------------------------|
| phone_number   | string  | *        | Enter phone_number                               |

### Response

| Parameter      | Type    | Description                                     |
|----------------|---------|-------------------------------------------------|
| status         | string  | Can be `success` or `error`.                   |
| message        | string  | A message saying whether the deletion succeeded, or a helpful message describing why it failed. |

cURL
curl --request POST \
  --url https://api.bland.ai/v1/inbound/{phone_number}/delete \
  --header 'authorization: <authorization>' \
  --header 'encrypted_key: <encrypted_key>'

Response
{
  "status": "success",
  "message": "Successfully deleted number from database: +15555555555"
}


### Batches
#### Send a Batch of Calls
Send large volumes of calls at once with a single API request.

### Endpoint

`POST /v1/batches`

### Header

| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Body

| Parameter      | Type    | Required | Description                                                                                  |
|----------------|---------|----------|----------------------------------------------------------------------------------------------|
| base_prompt    | string  | *        | Enter base_prompt. This is the prompt or task used for all the phone calls in the request. Information can be inserted into it surrounding variable names with {{curly braces}}. |
| call_data      | array   | *        | Define a list of calls to make and their properties. Each call in call_data MUST have a “phone_number” property. |

#### Example 
"You are calling {{business}} to renew their subscription to {{service}} before it expires on {{date}}."


| Parameter      | Type    | Required | Description                                                                                  |
|----------------|---------|----------|----------------------------------------------------------------------------------------------|
| call_data      | array   | *        | Define a list of calls to make and their properties. Each call in call_data MUST have a “phone_number” property. Properties are case-sensitive. |

#### Example
[
  {   
    "phone_number": "1234567890",
    "business": "ABC Corp",
    "service": "Netflix",
    "date": "September 4th"
  },
  {
    "phone_number": "32176540987",
    "business": "XYZ inc.",
    "service": "Window Cleaning",
    "date": "December 20th"
  }
]

| Parameter      | Type      | Required | Description                                                                                  |
|----------------|-----------|----------|----------------------------------------------------------------------------------------------|
| from           | string    |          | Use a purchased number to send batch calls from. We do not recommend this for large batches as there is risk of your number getting flagged for spam. |
| label          | string    |          | Adds a user-friendly label to your batch to keep track of its original intention. This can help differentiate multiple call batches that are part of the same Campaign. Shown when a batch is retrieved. |
| campaign_id    | string    |          | Use campaign_id to organize related batches together. This can be set manually or auto-generated through Campaigns. |
| test_mode      | boolean   |          | Default: `false`. When this is set to true, only the first call of call_data will be dispatched. A common use case is to set the first phone_number value to your own to confirm everything’s set up properly. Includes additional information in the response when true so that it’s easier to find any issues. |
| *              |           |          | All other parameters supported by the Send Call endpoint are supported here as well. They will be applied to each call in the batch. |
| batch_webhook  | string    |          | A URL that will receive a POST request when the batch is completed. The request will include the batch_id and the status of the batch. |

### Response
| Parameter      | Type      | Description                                     |
|----------------|-----------|-------------------------------------------------|
| message        | string    | If anything other than “success” is returned, there was an error. |
| batch_id       | string    | The unique identifier for the batch.           |


cURL
curl --request POST \
  --url https://api.bland.ai/v1/batches \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "base_prompt": "<string>",
  "call_data": [
    {}
  ],
  "from": "<string>",
  "label": "<string>",
  "campaign_id": "<string>",
  "test_mode": true
}'

Response
{
    "message": "success",
    "batch_id": "3p$7rQ3p9sT5bzmF-gen-batch"
}


## Batches
### Analyze Batch with AI
Analyzes a batch of calls based on using questions and goals.

### Endpoint

`POST /v1/batches/{batch_id}/analyze`

### Header
| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Path Parameters
| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| batch_id       | string | *        | Enter batch_id                                   |

### Body Parameters
| Parameter      | Type    | Required | Description                                                                                  |
|----------------|---------|----------|----------------------------------------------------------------------------------------------|
| goal           | string  | *        | This is the overall purpose of the batch of calls. Provides context for the analysis to guide how the questions/transcripts are interpreted. |
| questions      | array   | *        | An array of questions to be analyzed for each call in the batch. Each question should be an array with two elements: the question text and the expected answer type (e.g., “string”, “boolean”). |

#### Example
"questions": [
      ["Who answered the call?", "human or voicemail"],
      ["Positive feedback about the product: ", "string"],
      ["Negative feedback about the product: ", "string"],
      ["Customer confirmed they were satisfied", "boolean"]
  ]

  ## Response

  | Parameter      | Type    | Description                                                                                     |
  |----------------|---------|-------------------------------------------------------------------------------------------------|
  | status         | object  | Will be success if the request was successful.                                                 |
  | message        | string  | Confirms the request was successful, or provides an error message if the request failed.      |
  | answers        | object  | Contains the analyzed answers for each call in the batch. The keys are call_ids from the batch, and the array values are the analysis results for each question in the batch. |
  | credits_used   | number  | Token-based price for the analysis request. As a rough estimate, the base cost is 0.003 credits with an additional 0.0015 credits per call in the batch. Longer call transcripts and higher numbers of questions can increase the cost, however the cost scales very effectively with batches vs. individual calls. |


cURL
curl --request POST \
  --url https://api.bland.ai/v1/batches/{batch_id}/analyze \
  --header 'Content-Type: application/json' \
  --header 'authorization: <authorization>' \
  --data '{
  "goal": "<string>",
  "questions": [
    [
      "<string>"
    ]
  ]
}'

Response
{
    "status": "success",
    "message": "Successfully analyzed batch",
    "answers": {
        "123e4567-e89b-12d3-a456-426614174000": [
            "human",
            "Customer found the product sturdy and reliable",
            "A bit heavy",
            true
        ],
        "123e4567-e89b-12d3-a456-426614174001": [
            "voicemail",
            null,
            null,
            false
        ]
    }
}

### Batches
#### Stop Active Batch
Stops all active calls in a batch.

### Endpoint
`POST /v1/batches/{batch_id}/stop`

### Header
| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Path Parameters
| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| batch_id       | string | *        | Enter batch_id                                   |

### Response
| Parameter      | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| status         | string  | The status of the request. If anything other than ‘success’, an error has occurred or all calls have already been completed. |
| message        | string  | A message describing the status of the request.  |
| num_calls      | number  | The number of calls that were cancelled.        |
| batch_id       | array   | The batch_id of the cancelled batch.            |

curl --request POST \
  --url https://api.bland.ai/v1/batches/{batch_id}/stop \
  --header 'authorization: <authorization>'

Response
{
  "status": "success",
  "message": "Successfully stopped batch",
  "num_calls": 1205,
  "batch_id": "5e5b1a3a-2b0a-4b9e-8b9e-asdf-gen-batch"
}


### Batches
#### List Batches
Retrieves batch-specific data for each batch you’ve created.

### Endpoint
`GET /v1/batches`

### Header
| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

### Query Parameters
| Parameter      | Type    | Required | Description                                    |
|----------------|---------|----------|------------------------------------------------|
| campaign_id    | string  |          | Retrieve only batches with a specific campaign ID. |
| from           | integer |          | The starting index (inclusive) for the range of batches to retrieve. |
| to             | integer |          | The ending index for the range of batches to retrieve. |
| limit          | integer |          | Default: `1000`. The maximum number of batches to return in the response. |
| ascending      | boolean |          | Default: `false`. Whether to sort the batches in ascending order of their creation time. |

### Response
| Parameter      | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| status         | string  | Can be `success` or `error`.                    |
| batches        | array   | Contains an array of batch objects.              |
| batches[i].batch_id       | string  | The unique identifier for the batch.            |
| batches[i].base_prompt    | string  | The original base prompt used to create the batch. Will still contain the original placeholder variables such as `{{ business }}` or `{{ name }}`. |
| batches[i].label          | string  | The label you assigned to the batch (if any).   |
| batches[i].endpoint_code  | string  | Default: `API`. Enterprise customers with custom endpoints will see the endpoint code here (if specified). |
| batches[i].call_params    | array   | The base call parameters used to create the batch, such as `voice_id`, `max_duration`, `reduce_latency`, and `wait_for_greeting`. |
| batches[i].created_at     | string  | The date and time the batch was created.       |


cURL
curl --request GET \
  --url https://api.bland.ai/v1/batches \
  --header 'authorization: <authorization>'

Response
{
    "status": "success",
    "batches": [
        {
            "batch_id": "ZfowpkhOSVCZJ94i-gen-batch",
            "campaign_id": "a2shduf92f74p8288c93nid5",
            "created_at": "2023-11-16T22:14:24.9663+00:00",
            "label": "Subscription Renewal Reminders",
            "base_prompt": "You are calling {{business}} and need to let them know that their subscription to {{service}} is going to expire on {{date}}. If they'd like to renew, take their credit card information and bill them through {{url}}",
            "endpoint_code": "api",
            "call_params": {
                "reduce_latency": true,
                "voice_id": 2,
                "language": "eng",
                "request_data": {
                    "test_param": "request data.test_param",
                    "your name": "Janessa"
                },
                "max_duration": 5,
                "wait_for_greeting": false
            }
        },
        //...
    ]
}


## Batches
### Batch Details
Retrieves calls and batch data for a specific batch_id.

#### GET
`/v1/batches/{batch_id}`

#### Header
| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

#### Path
| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| batch_id       | string | *        | Enter batch_id                                   |

#### Query
| Parameter              | Type     | Default   | Description                                      |
|------------------------|----------|-----------|--------------------------------------------------|
| include_calls          | boolean  | true      | Whether or not to include individual call data in the response. |
| include_transcripts    | boolean  | true      | If calls are included, can be set to false to exclude transcripts from the response. |
| include_analysis       | boolean  | true      | If calls are included, can be set to false to exclude analysis from the response. |

#### Response
| Parameter      | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| status         | string  | The status of the batch. Possible values are in-progress and completed. |
|                |         | in-progress: The batch is still in progress.    |
|                |         | completed: Every call in the batch has completed. |
| batch_params   | object  | An object containing parameters and settings for the batch. |
| batch_params.id| string  | The unique identifier of the batch - used as the batch_id parameter in other API calls. |
| batch_params.created_at | string | The creation timestamp of the batch. |
| batch_params.label | string | The label or description of the batch. |
| batch_params.base_prompt | string | The base prompt used for calls in this batch. |
| batch_params.endpoint_code | string | The endpoint code used for API integration. |
| batch_params.call_params | object | An object containing parameters for the calls in the batch. |
| analysis       | object  | An object containing analysis data for the batch. |
| analysis.total_calls | object | The total number of calls in the batch, including completed and in-progress calls. |
| analysis.completed_calls | object | The total number of completed calls in the batch. |
| analysis.in_progress_calls | object | The total number of in-progress calls in the batch. |
| analysis.queue_statuses | object | An object containing the number of calls in each queue status. |

Example:
{
  "complete": 237,
  "queued": 2,
  "call_error": 1
}

### analysis.call_lengths
- **Type:** object  
- **Description:** Contains average, average_nonzero, summary, and all fields.

  - **average:** The average call length in minutes.
  - **average_nonzero:** The average call length in minutes, excluding calls with a length of less than one second.
  - **summary:** A summary of the call lengths, grouped into ranges.
  - **all:** Contains each call length, in case you want to use a different grouping than the default.

### analysis.call_ids
- **Type:** array  
- **Description:** Contains each call_id in the batch.

### analysis.error_messages
- **Type:** array  
- **Description:** Contains any error messages that calls in the batch may have.

  **Example:**
  ```json
  [
    {
      "call_id": "c52f5f8c-147e-478c-4b40-88214feeba29",
      "error_message": "Cannot transfer to +12223334444 - Call is no longer active"
    }
  ]
  ```

### analysis.endpoints
- **Type:** object  
- **Description:** Contains the number of calls that have been sent to each endpoint. Applicable only to API integrations.

### call_data
- **Type:** array  
- **Description:** An array of objects, each representing individual call data.

  - **call_data[].created_at:**  
    - **Type:** string  
    - **Description:** The timestamp when the individual call was created.

  - **call_data[].to:**  
    - **Type:** string  
    - **Description:** The phone number the call was made to.

  - **call_data[].from:**  
    - **Type:** string  
    - **Description:** The phone number the call was made from.

  - **call_data[].completed:**  
    - **Type:** boolean  
    - **Description:** Indicates if the call was completed.

  - **call_data[].call_id:**  
    - **Type:** string  
    - **Description:** The unique identifier for each individual call.

  - **call_data[].call_length:**  
    - **Type:** number  
    - **Description:** The duration of the call in minutes.

  - **call_data[].answered_by:**  
    - **Type:** array  
    - **Description:** Contains a string value if the batch had answered_by_enabled set to true.

    **Values:**
    - voicemail
    - human
    - unknown
    - no-answer
    - null


cURL
curl --request GET \
  --url https://api.bland.ai/v1/batches/{batch_id} \
  --header 'authorization: <authorization>'

Response
{
  "status": "in-progress",
  "batch_params": {
    "id": "AAcQq8zXxLB56LWg-gen-batch",
    "campaign_id": null,
    "created_at": "2023-12-07T20:43:44.544773+00:00",
    "label": "Customer Satisfaction Follow-up",
    "base_prompt": "You are calling {{name}} about their recent purchase of the item: {{item}}. Ask them each of the following questions about the specific item they purchased: {{questions}}",
    "endpoint_code": "api",
    "call_params": {
      "reduce_latency": true,
      "voice_id": 0,
      "language": "eng",
      "max_duration": 10,
      "wait_for_greeting": false
    }
  },
  "call_data": [
      {
          "status": "completed",
          "corrected_duration": "12",
          "end_at": "2023-12-16T00:17:38.000Z",
          "call_id": "ffa99be3-63dd-44dc-9523-380cd25c1b9e",
          "to": "1112223333",
          "from": "+17473423273",
          "completed": true,
          "created_at": "2023-12-16T00:17:22.383682+00:00",
          "queue_status": "complete",
          "endpoint_url": "api.bland.ai",
          "max_duration": 30,
          "error_message": null,
          "answered_by": "voicemail",
          "request_data": {
              "phone_number": "1112223333",
              "reduce_latency": true,
              "wait": false,
              "language": "ENG"
          },
          "transcripts": [
              {
                  "id": 1188954,
                  "created_at": "2023-12-16T00:17:30.46833+00:00",
                  "text": " Hi, Im calling about the laundromat for sale.  —  ",
                  "user": "assistant",
                  "c_id": "ffa99be3-63dd-44dc-9523-380cd25c1b9e"
              },
              {
                  "id": 1188957,
                  "created_at": "2023-12-16T00:17:35.14056+00:00",
                  "text": "I'll get back to you as soon as you can. Just leave a message. Thank you. Bye.",
                  "user": "user",
                  "c_id": "ffa99be3-63dd-44dc-9523-380cd25c1b9e"
              },
              {
                  "id": 1188959,
                  "created_at": "2023-12-16T00:17:36.710551+00:00",
                  "text": "Ended call: Goodbye",
                  "user": "agent-action",
                  "c_id": "ffa99be3-63dd-44dc-9523-380cd25c1b9e"
              }
          ],
          "call_length": 0.12345
      },  
    //...
  ],
    "analysis": {
      "total_calls": 88,
      "completed_calls": 86,
      "in_progress_calls": 2,
      "queue_statuses": {
          "complete": 85,
          "started": 2,
          "call_error": 1
      },
      "call_lengths": {
          "average": 17,
          "average_nonzero": 31, 
          "summary": {
              "0-5": 18,
              "5-10": 4,
              "10-15": 3,
              "15-20": 2,
              "20-30": 14,
              "30-45": 28,
              "45-60": 11,
              "60-90": 6,
              "90-120": 1,
              "120+": 1
          },
          "all": [
              7,
              32,
              //...
          ]
      },
      "call_ids": [
          "ffa99be3-63dd-44dc-9523-380cd25c1b9e",
          "591338a8-34b2-41e6-93da-b9029c9bdedc",
          //...
      ],
      "error_messages": [
        {
          "call_id": "c52f5f8c-147e-478c-4b40-88214feeba29",
          "error_message": "Cannot transfer to +12223334444 - Call is no longer active"
        }
      ],
      "endpoints": {
        "api.bland.ai": 88
      }
  }
}


### Batches
#### Retrieve Batch Analysis
Retrieves the analyses for a specific batch of calls, including details of each call’s analysis.

**GET**  
`/v1/batches/{batch_id}/analysis`

**Header**
| Key            | Type   | Required | Description               |
|----------------|--------|----------|---------------------------|
| authorization  | string | *        | Enter authorization        |

**Path**
| Parameter      | Type   | Required | Description                                    |
|----------------|--------|----------|------------------------------------------------|
| batch_id       | string | *        | Enter batch_id                                   |

**Response**
| Parameter      | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| status         | string  | Whether the request was successful or not. Possible values are `success` and `error`. |
| message        | string  | An error message or confirmation that the request was successful. |
| analysis       | array   | An array of analysis objects, each corresponding to a call within the batch. |

Each analysis object includes:
- **call_id**
- **batch_id**
- **goal**
- **answers** - the results of the AI analysis
- **questions** - the original questions asked by the AI

cURL
curl --request GET \
  --url https://api.bland.ai/v1/batches/{batch_id}/analysis \
  --header 'authorization: <authorization>'

Response
{
    "status": "success",
    "message": "Successfully fetched analyses",
    "analysis": [
        {
            "call_id": "b12956d1-624d-4c65-a1a4-30eb86553c85",
            "batch_id": "dnytTRqwiqnR3qmq-gen-batch",
            "goal": "Congratulate some employees",
            "answers": [
                "human",
                "Customer found the product sturdy and reliable",
                "A bit heavy",
                true
            ],
            "questions": [
                ["Who answered the call?", "human or voicemail"],
                ["Positive feedback about the product: ", "string"],
                ["Negative feedback about the product: ", "string"],
                ["Customer confirmed they were satisfied", "boolean"]
            ]
        },
        // Additional analysis objects...
    ]
}



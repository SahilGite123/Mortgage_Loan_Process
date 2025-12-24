# TCS_Mortgage

AI-Assisted Property Valuation using MCP (Model Context Protocol)
**Overview**

This project implements an AI-assisted property valuation system using the Model Context Protocol (MCP) architecture.

The system estimates the indicative market value of a property by combining:

Location data

Nearby infrastructure

Visual surroundings

AI-based reasoning

Important:
GenAI is not used to directly execute actions or call APIs.
All execution is strictly controlled by the MCP layer.

**Problem Statement**

Traditional property valuation systems are either:

Fully rule-based (fixed weights, static logic), or

Fully manual (human surveyors)

Our goal is to design a system where:

GenAI handles decision-making and reasoning

MCP enforces execution control

External APIs provide real-world data

This aligns with how enterprise-grade AI systems are designed.

**Key Design Principle**

GenAI thinks. MCP controls. Agents execute.

High-Level Architecture
Client
  |
  v
FastAPI Endpoint (/mcp/start)
  |
  v
MCP Router (Orchestrator)
  |
  +--> Workflow Agent (GenAI - Planning)
  |
  +--> Data Collector Agent (Maps & Places APIs)
  |
  +--> Vision Agent (Street View / Imagery)
  |
  +--> Valuation Agent (GenAI - Reasoning)
  |
  v
Final Unified Response

**MCP Workflow (Step-by-Step)**
1. Client Request

The client sends a property-related request (e.g. address).

Example:

{
  "address": "Nashik, Maharashtra"
}

2. MCP Entry Point

The request enters the system through:

POST /mcp/start


This is where the MCP lifecycle begins.

3. Workflow Agent (GenAI – Planning)

Uses GenAI to analyze the input context

Decides:

Whether location data is needed

Whether visual verification is required

Whether valuation is feasible

GenAI does not call APIs
GenAI only returns a structured plan

4. MCP Router (Execution Control)

The MCP Router:

Reads the GenAI decision

Selectively triggers only the required agents

Enforces execution order

Prevents uncontrolled execution

5. Data Collector Agent (Deterministic)

Uses:

Google Maps API

Google Places API

Fetches:

Latitude & longitude

Nearby amenities (hospitals, schools, IT parks, etc.)

6. Vision Agent (Perception)

Uses:

Street-level imagery (Google Street View)

Provides:

Qualitative observations (road access, surroundings)

Vision Agent does not estimate price

7. Valuation Agent (GenAI – Reasoning)

Uses GenAI to:

Combine structured data + vision context

Produce:

Estimated property value

Reasoning

Confidence level

GenAI does not fetch data
GenAI does not execute APIs

**Where GenAI Is Used (Explicitly)**

GenAI is used only in two places:

Agent	Purpose
Workflow Agent	Planning & decision-making
Valuation Agent	Reasoning & explanation

All execution is handled by MCP-controlled agents.

**Security & Control (Why MCP)**

API keys are stored in environment variables

GenAI never sees API keys

GenAI never executes code

MCP enforces strict execution boundaries

This mirrors real-world enterprise AI safety practices.


**Environment Variables**

Create a .env file with:

OPENAI_API_KEY=your_openai_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key

How to Run the Project
1. Install dependencies
pip install -r requirements.txt

2. Start the server
uvicorn app.main:app --reload

3. Call the MCP endpoint
POST http://127.0.0.1:8000/mcp/start

**Output Example**
{
  "estimated_value_in_inr": 8500000,
  "valuation_reasoning": "...",
  "confidence_level": "medium"
}

**Limitations**

Government land registry APIs are not publicly available

Vision analysis is contextual, not authoritative

Generic addresses lead to low-confidence estimates

**Future Enhancements**

Integration with official land rate APIs

Deterministic confidence scoring

PDF valuation report generation

Caching and rate-limit handling
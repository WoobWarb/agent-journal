# System

> How this project works -- the part the code alone does not make obvious.
> AI agents: read this before changing anything that crosses a component boundary,
> and update it in the same task whenever one of these facts changes.
> Delete sections that do not apply. Keep it short: facts, not history (history goes in Agent-Journal.md).

## Overview

<!-- One paragraph: what the system does and for whom. -->

## Architecture

<!-- The components and how they talk to each other. A small diagram is enough, e.g.

  [Device firmware] <--WebSocket--> [Server] <--HTTPS--> [Cloud API]
-->

| Component | Where it lives | Role |
|-----------|----------------|------|
|           |                |      |

## Interfaces & Protocols

<!-- Every contract between components: HTTP endpoints, WebSocket/serial/MQTT messages, file formats.
     Give the exact format and one example for each. -->

| Interface | Direction | Format / example | Meaning |
|-----------|-----------|------------------|---------|
|           |           |                  |         |

## Hardware & Environment

<!-- Boards, pin assignments, OS, runtime versions, required libraries and their versions. -->

| Item | Value | Notes |
|------|-------|-------|
|      |       |       |

## Critical Config

<!-- Values that break the system when wrong, especially ones that must match in more than one place
     (protocol versions, ports, baud rates, feature flags). Say where each one is defined. -->

| Setting | Defined in | Must match | Why it matters |
|---------|------------|------------|----------------|
|         |            |            |                |

## Secrets

<!-- Where secrets live and how to obtain them. NEVER write a secret value in this file
     or anywhere else under .agents/ -- only its name and location. -->

| Secret | Stored in | Used by |
|--------|-----------|---------|
|        |           |         |

## Known Limits

<!-- Constraints that are not bugs: memory limits, rate limits, unsupported cases. -->

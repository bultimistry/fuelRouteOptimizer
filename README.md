# Fuel Route Optimizer API

## Overview

This project is a Django REST API that calculates optimized fuel stops for road trips within the USA.

Features:
- Route calculation
- Fuel optimization
- Fuel cost estimation
- 500-mile vehicle range support
- Map visualization

## Technologies

- Django
- Django REST Framework
- OpenRouteService
- Leaflet.js
- SQLite

## API Endpoint

POST /api/route/

Example Request:

{
  "start": "New York",
  "finish": "Chicago"
}

## Assumptions

- Vehicle MPG = 10
- Vehicle maximum range = 500 miles

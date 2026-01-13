# LATE SHOWS CODE CHALLENGE

A comprehensive Flask REST API for managing late show episodes, guests, and their appearances. This application provides a complete backend solution for tracking television show data with full CRUD operations and proper data relationships.

## Project Overview

This project implements a many-to-many relationship between Episodes and Guests through an Appearance join table. The API allows users to manage show episodes, celebrity guests, and track guest appearances with ratings. Built with Flask and SQLAlchemy, it follows RESTful principles and includes proper error handling and data validation.

## Features

- **Episode Management**: Create and retrieve episodes with unique dates and episode numbers
- **Guest Management**: Store guest information including names and occupations
- **Appearance Tracking**: Record guest appearances on specific episodes with user ratings
- **Data Relationships**: Proper many-to-many relationships with cascade delete functionality
- **Input Validation**: Server-side validation for rating values (1-5 scale)
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes
- **JSON Serialization**: Clean JSON responses with controlled serialization depth
- **Database Migrations**: Flask-Migrate integration for database schema management


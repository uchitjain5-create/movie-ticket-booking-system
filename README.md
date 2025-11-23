Theatre Management System 🎬

A robust, console-based Python application designed to simulate a movie theatre ticketing system. This program allows users to view available shows, book tickets, and cancel reservations through an interactive command-line interface.

📋 Features

View Shows: Display a list of currently running movies, including duration and real-time seat availability.

Book Tickets: Reserve a specific number of seats for a chosen movie.

Validation: Prevents booking more seats than available.

Validation: Prevents invalid inputs (negative numbers, non-numeric text).

Cancel Tickets: Cancel previously booked tickets and free up seats.

Validation: Prevents cancelling more seats than are currently booked.

Data Integrity: Automatically handles seat count updates (decrementing on booking, incrementing on cancellation).

Case Insensitivity: Recognizes movie titles regardless of capitalization (e.g., "rrr", "RRR", "Rrr").

🚀 Getting Started

Prerequisites

Python 3.x installed on your machine.

Installation & Running

Save the code: Save the provided Python code into a file named theatre_system.py.

Open Terminal/Command Prompt: Navigate to the directory where you saved the file.

Run the application:

python theatre_system.py


🎮 Usage Guide

Upon running the program, you will see the following menu:

1 --> View shows
2 --> Book tickets
3 --> Cancel tickets
4 --> Quit


Select an Option: Enter the number corresponding to your desired action (1-4).

Follow Prompts:

If Booking/Cancelling: Enter the exact movie name (e.g., "Sholay") and the number of seats.

The system will confirm success or provide an error message (e.g., "Unable to book...").

🏗️ Code Structure

The application is built using Object-Oriented Programming (OOP) principles:

1. Class: Show

Represents a single movie screening.

Attributes: title, time, total_seats, booked_seats.

Methods:

book_seats(n): Logic to add bookings.

cancel_seats(n): Logic to remove bookings.

available_seat(): Returns current availability.

2. Class: Theatre

Manages the collection of shows.

Attributes: shows (list of Show objects).

Methods:

add_show(show): Adds a new movie to the theatre.

book_ticket(title, count): Searches for a movie and triggers the booking.

cancel_tickets(title, count): Searches for a movie and triggers cancellation.

3. Function: run_theatre()

The entry point of the application. It initializes the data (adds movies like Sholay, RRR, KGF, Pushpa) and contains the while True loop for user interaction.

🔮 Future Improvements

Seat Mapping: Add specific seat selection (e.g., Row A, Seat 1).

Pricing: Calculate total cost based on ticket price.

Data Persistence: Save booking data to a file so it remains after closing the program.
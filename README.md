# NammaGYM : Gym Management System

Made as part of the final project for UE21CS351A.

## Features

- Member Management: Add, view, update, and delete member details.
- Trainer Management: Manage details of gym trainers.
- Class Management: View and manage fitness classes, including instructor details.
- Payments and Invoices: Record member payments and generate invoices.
- Equipment Management: Track gym equipment details.
- Attendance Tracking: Keep track of member attendance in classes.
- Custom Query: Execute custom SQL queries and view the results.
- Dashboard Metrics: Overview of gym metrics, including total members, active memberships, upcoming classes.


## Steps to Run

1. Execute the SQL scripts in the "/db" folder in the following order:
    - `database.sql`
    - `activemembers_procedure.sql`
    - `data.sql`
    - `payment_trigger.sql`

2. Create a `.env` file in the project root directory with your MySQL database password. Add the following line:
    ```
    PASSWORD=your_password
    ```

3. Install the necessary Node.js dependencies:
    ```bash
    npm install
    ```

4. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:
    ```bash
    flask run
    ```

6. Access the website by navigating to [http://localhost:5000](http://localhost:5000) in your web browser.

This setup assumes you have Node.js and npm installed for frontend dependencies and a MySQL server running with the appropriate configuration. Make sure to replace `your_password` in step 2 with your actual MySQL password.

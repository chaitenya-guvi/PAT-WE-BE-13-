-- SQL script for sample database
CREATE DATABASE IF NOT EXISTS SampleDB;
USE SampleDB;

-- Customers table
CREATE TABLE Customers (
    CustomerID VARCHAR(10) PRIMARY KEY,
    CustomerName VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    City VARCHAR(50)
);

-- Products table
CREATE TABLE Products (
    ProductID VARCHAR(10) PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    Stock INT
);

-- Shippers table
CREATE TABLE Shippers (
    ShipperID VARCHAR(10) PRIMARY KEY,
    ShipperName VARCHAR(100),
    Phone VARCHAR(15),
    Country VARCHAR(50)
);

-- Orders table
CREATE TABLE Orders (
    OrderID VARCHAR(10) PRIMARY KEY,
    CustomerID VARCHAR(10),
    ProductID VARCHAR(10),
    ShipperID VARCHAR(10),
    OrderDate DATE,
    Quantity INT,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (ShipperID) REFERENCES Shippers(ShipperID)
);

-- Insert data into Customers
INSERT INTO Customers (CustomerID, CustomerName, Email, Phone, City) VALUES
('CUST001', 'John Doe', 'john@example.com', '9876543210', 'New York'),
('CUST002', 'Jane Smith', 'jane@example.com', '9876543211', 'Los Angeles'),
('CUST003', 'Michael Johnson', 'michael@example.com', '9876543212', 'Chicago'),
('CUST004', 'Emily Davis', 'emily@example.com', '9876543213', 'Houston'),
('CUST005', 'Chris Lee', 'chris@example.com', '9876543214', 'Phoenix'),
('CUST006', 'Sarah Brown', 'sarah@example.com', '9876543215', 'Philadelphia'),
('CUST007', 'David Wilson', 'david@example.com', '9876543216', 'San Antonio'),
('CUST008', 'Laura Clark', 'laura@example.com', '9876543217', 'San Diego'),
('CUST009', 'Daniel Lewis', 'daniel@example.com', '9876543218', 'Dallas'),
('CUST010', 'Sophia Hall', 'sophia@example.com', '9876543219', 'San Jose');

-- Insert data into Products
INSERT INTO Products (ProductID, ProductName, Category, Price, Stock) VALUES
('PRD001', 'Laptop', 'Electronics', 800, 50),
('PRD002', 'Smartphone', 'Electronics', 600, 120),
('PRD003', 'Tablet', 'Electronics', 300, 80),
('PRD004', 'Monitor', 'Accessories', 200, 60),
('PRD005', 'Keyboard', 'Accessories', 50, 200),
('PRD006', 'Mouse', 'Accessories', 25, 250),
('PRD007', 'Headphones', 'Audio', 75, 100),
('PRD008', 'Camera', 'Photography', 500, 40),
('PRD009', 'Printer', 'Office', 150, 30),
('PRD010', 'Router', 'Networking', 100, 90);

-- Insert data into Shippers
INSERT INTO Shippers (ShipperID, ShipperName, Phone, Country) VALUES
('SHP001', 'FastShip', '9123456780', 'USA'),
('SHP002', 'QuickExpress', '9123456781', 'USA'),
('SHP003', 'GlobalDelivery', '9123456782', 'UK'),
('SHP004', 'RapidCourier', '9123456783', 'Canada'),
('SHP005', 'SpeedyShip', '9123456784', 'Germany'),
('SHP006', 'EliteLogistics', '9123456785', 'France'),
('SHP007', 'SwiftTransport', '9123456786', 'Australia'),
('SHP008', 'PrimeDelivery', '9123456787', 'India'),
('SHP009', 'SafeMove', '9123456788', 'Japan'),
('SHP010', 'OnTimeExpress', '9123456789', 'Brazil');

-- Insert data into Orders
INSERT INTO Orders (OrderID, CustomerID, ProductID, ShipperID, OrderDate, Quantity, TotalAmount) VALUES
('ORD001', 'CUST001', 'PRD001', 'SHP001', '2025-10-01', 2, 1600),
('ORD002', 'CUST002', 'PRD002', 'SHP002', '2025-10-02', 1, 600),
('ORD003', 'CUST003', 'PRD003', 'SHP003', '2025-10-03', 3, 900),
('ORD004', 'CUST004', 'PRD004', 'SHP004', '2025-10-04', 5, 1000),
('ORD005', 'CUST005', 'PRD005', 'SHP005', '2025-10-05', 1, 50),
('ORD006', 'CUST006', 'PRD006', 'SHP006', '2025-10-06', 4, 100),
('ORD007', 'CUST007', 'PRD007', 'SHP007', '2025-10-07', 2, 150),
('ORD008', 'CUST008', 'PRD008', 'SHP008', '2025-10-08', 1, 500),
('ORD009', 'CUST009', 'PRD009', 'SHP009', '2025-10-09', 6, 900),
('ORD010', 'CUST010', 'PRD010', 'SHP010', '2025-10-10', 2, 200);

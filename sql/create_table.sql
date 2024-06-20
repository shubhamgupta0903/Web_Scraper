-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS internship_project;

-- Use the created database
USE internship_project;

-- Create the 'website_info' table if it does not already exist
CREATE TABLE IF NOT EXISTS website_info (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- Primary key with auto-increment
    website_url VARCHAR(255),                 -- URL of the website
    robots_url VARCHAR(255),                  -- URL of the robots.txt file
    sitemap_url VARCHAR(255),                 -- URL of the sitemap
    contact_email VARCHAR(255),               -- Contact email address
    contact_address VARCHAR(255),             -- Contact physical address
    contact_number VARCHAR(255),              -- Contact phone number
    language VARCHAR(255),                    -- Language of the website
    cms VARCHAR(255),                         -- Content Management System (CMS) used
    mvc VARCHAR(255),                         -- Model-View-Controller (MVC) framework used
    category VARCHAR(255)                     -- Category of the website
);

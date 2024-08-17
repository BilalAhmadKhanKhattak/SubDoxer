# SubHunter

## Overview

**SubHunter** is a Python tool designed to discover subdomains associated with a target domain. Ideal for cybersecurity enthusiasts and penetration testers, this tool helps you map out potential subdomains quickly and efficiently.

Version 1.1 of SubHunter utilizes a predefined list of over 500 common and potential subdomains to check against a target domain. It employs DNS resolution to verify the existence of these subdomains.

## Features

- **DNS Resolution**: Uses DNS 'A' record checks to verify subdomain existence.
- **Multithreading**: Accelerates the process using concurrent threads.
- **Extensive Subdomain List**: Includes over 500 predefined subdomains.
- **Customizable**: Easily extendable with additional subdomains.
- **Colorful Output**: Provides clear and colorful console output using `colorama`.


![image](https://github.com/BilalAhmadKhanKhattak/SubHunter/blob/main/Screenshot%20(14).png)
## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BilalAhmadKhanKhattak/SubHunter.git
    cd SubHunter
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** `requirements.txt` should include:

    ```
    dnspython
    colorama
    ```

## Usage

1. **Run the tool:**

    ```bash
    python subhunter.py
    ```

2. **Enter the target domain when prompted:**

    ```
    Enter The Domain: example.com
    ```

3. **Review the discovered subdomains listed in the console output.**

## Example Output

```
Enter The Domain: example.com

Valid Subdomains For example.com:
1. www.example.com
2. mail.example.com
3. api.example.com
...
```

## Code Explanation

- **`check_subdomain(subdomain, domain_to_be_processed)`**: Checks if a subdomain exists by resolving its DNS 'A' record.
- **`enumerate_subdomains(domain_to_be_processed)`**: Iterates through a predefined list of over 500 subdomains to identify existing ones.

## License

This project is licensed - see the [LICENSE](LICENSE) file for details.

## Author

**MR BILRED** (Bilal Ahmad Khan Khattak)  
[GitHub Profile](https://github.com/BilalAhmadKhanKhattak)  

---

# SubDoxer

## Overview

**SubDoxer** is a Python tool designed to discover subdomains associated with a target domain. Ideal for cybersecurity enthusiasts and penetration testers, this tool helps you map out potential subdomains quickly and efficiently.

Version 1.1 of SubDoxer utilizes a predefined list of over 500 common and potential subdomains to check against a target domain. It employs DNS resolution to verify the existence of these subdomains.

# What’s New in SubDoxer v2.0?

A major upgrade from v1.1 with smarter features, faster execution, and more advanced OSINT capabilities.

## Major Changes & Improvements

| Feature               | Version 1.1               | Version 2.0                                      |
|-----------------------|---------------------------|--------------------------------------------------|
| **Subdomain Source**   | Predefined list only     | Now also uses **crt.sh** to pull real subdomains from SSL certs |
| **Resolution Method**  | DNS `A` record check     | Still supported |
| **Multithreading**     | Basic or none            | Uses `concurrent.futures` for **fast DNS resolution** |
| **Cert Fetching**      | ❌ Not available         | ✅ Pulls JSON data from [crt.sh](https://crt.sh), saves it |
| **Subdomain Output**   | Console only             | JSON saved + TXT file export                      |
| **User Agent Randomization** | ❌                 | ✅ Randomizes headers for stealthy requests       |
| **Error Handling**     | Minimal                  | Improved error reporting, retries on failures    |
| **Banner & UI**        | Basic                    | Upgraded ASCII art + styled messages using `colorama` |
| **Developer Note**     | None                     | uhmm yeah!     |
| **Version Control**    | v1.1                     | **v2.0**                    |

## Capabilities
- 💥 **crt.sh Integration:** Extracts subdomains by parsing public certificate transparency logs.
- 📁 **Automatic JSON & TXT Saving:** Store your discoveries for later analysis.
- 🧵 **Multithreaded Speed:** Uses 20 threads by default to resolve faster(used in v1.1 too).
- 🧠 **Smart Error Handling:** 3 retry attempts with user-agent randomness(3 useragents).

## Features in v1.1

- **DNS Resolution**: Uses DNS 'A' record checks to verify subdomain existence.
- **Multithreading**: Accelerates the process using concurrent threads.
- **Extensive Subdomain List**: Includes over 500 predefined subdomains.
- **Customizable**: Easily extendable with additional subdomains.
- **Colorful Output**: Provides clear and colorful console output using `colorama`.


![image](https://github.com/BilalAhmadKhanKhattak/SubDoxer/blob/main/Screenshot%20(25).png)
## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BilalAhmadKhanKhattak/SubDoxer.git
    cd SubDoxer
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
    python SubDoxer.py
    ```
    OR
   
    ```bash
    python Subdoxerv2.py
    ``` 

3. **Enter the target domain when prompted:**

    ```
    Enter The Domain: example.com
    ```

4. **Review the discovered subdomains listed in the console output.**

## Example Output(v1.1)

```
Enter The Domain: example.com

Valid Subdomains For example.com:
1. www.example.com
2. mail.example.com
3. api.example.com
...
```

## Code Explanation(v1.1)

- **`check_subdomain(subdomain, domain_to_be_processed)`**: Checks if a subdomain exists by resolving its DNS 'A' record.
- **`enumerate_subdomains(domain_to_be_processed)`**: Iterates through a predefined list of over 500 subdomains to identify existing ones.

## License

This project is licensed - see the [LICENSE](LICENSE) file for details.

## Author

**MR BILRED** (Bilal Ahmad Khan Khattak)  
[GitHub Profile](https://github.com/BilalAhmadKhanKhattak)  

---

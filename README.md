
# StrawPoll-AutoVote :ballot_box:

StrawPoll-AutoVote is a Python command line application designed to automate voting on StrawPolls. It utilizes proxy servers to distribute requests and allows for parallel execution to speed up the voting process. :rocket:

## Prerequisites :clipboard:

| Python Version | working        |
|----------------|----------------|
| 3.9            | no             |
| 3.10           | not tested yet |
| 3.11           | yes            |

Before using this application, make sure you have the following:

1. :snake: Python 3.11 installed on your system.
2. :page_facing_up: A list of proxy servers in a text file, e.g., `http_proxies.txt`, with each proxy formatted as `IP:Port` on a new line.

Example:
##### http_proxies.txt 
```
1.1.1.1:80
1.2.3.4:187
4.3.2.1:9999
...
```

## Installation :computer:

1. :open_file_folder: Clone this repository to your local machine.
2. :file_folder: Navigate to the repository's directory:
    
    ```bash
    cd StrawPoll-AutoVote
    ```
    
3. :package: Install the required dependencies using pip:
    
    ```bash
    pip3 install -r requirements.txt
    ```
    

## Usage :hammer_and_wrench:

To start the application, use the following command in your terminal:

```bash
python3 main.py --poll <poll_id> --vote <answer_id> --proxies http_proxies.txt --threads <num_threads>
```

Replace the placeholders with appropriate values:

-   `--poll`: The ID of the StrawPoll you want to vote on.
-   `--vote`: The ID of the answer option you want to vote for.
-   `--proxies`: The path to the proxy list text file.
-   `--threads`: The maximum number of threads to run in parallel. If not specified, the application will use the maximum available threads.

Example:

```bash
python3 main.py --poll kogjkj7d1Z6 --vote mpnbP4V5GZ5 --proxies http_proxies.txt --threads 24
```

Please note that excessive and inappropriate use of this application may violate the terms of use of StrawPoll or the proxy servers you are using. Use responsibly and respect the policies of the services involved. :warning:

### Where can i get vote ID?
![Drag Racing](https://i.ibb.co/0c6c6Fb/0815.gif)

## Disclaimer :warning:

This application is for educational and testing purposes only. The developers are not responsible for any misuse or violations resulting from the usage of this tool. Use at your own risk. :exclamation:

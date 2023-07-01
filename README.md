# Python_Port-Scanner
inspired by @Vinsloev Academy.
The provided Python code is a simple port scanning script that allows you to check if specific ports are open on a target host

Here's how to use the code above:

1. Make sure you have Python installed on your system.
2. Open a text editor or Python development environment (such as PyCharm or Jupyter Notebook) and create a new file.
3.Copy the Python code above and paste it into the newly created file.
4.Save the file with any name you want, for example "port_scanner.py".
5.Open a terminal or command prompt, then navigate to the directory where you saved the file "port_scanner.py".
6.Run the script by typing the following command in a terminal or command prompt:
7. bash
   python port_scanner.py

After you run the script, the scan results will be displayed in the terminal or command prompt.

Output examples:

less

    [ + ] Scan result of: www.google.com
    Scanning Port: 80
    [+]80 / tcp open
    Scanning Port: 22
    [+] 22/tcp closed

    In the example above, the script scans port 80 (HTTP) and port 22 (SSH) on the host www.google.com. the script indicates that port 80 is open and port 22 is closed.

You can change the target host and target port list as per your requirement by editing the portScan function call in the __name__ == '__main__'block. For example:

  python

  portScan('www.example.com', [80, 443, 3389])

In the example above, the script will scan port 80 (HTTP), port 443 (HTTPS), and port 3389 (RDP) on the host www.example.com.

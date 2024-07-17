# The "Asset Matcher" Interview Task
Domotz is looking for a talented, committed, and enthusiastic software engineer to take a pivotal role in expanding our product to greater heights.

To help us evaluate new talent, we have created this take-home interview question that should take you no more than a few hours.

**You must complete and submit the solution before the technical interview.**

### Why this interview format?
Traditional coding interviews can be intimidating and may not accurately reflect a candidate's abilities. By completing a take-home assignment, you can work in a more relaxed setting and demonstrate your true potential.

We aim is to ensure you feel comfortable and perform at your best.

### The Tech stack
At Domotz we are always striving to expand our tech stack but as specified in the job description the main languages/frameworks currently used include:
* Python
* JavaScript (TypeScript, NodeJS, AngularJS, React)

In this challenge you are free to use any of the above but sumissions in Go and Rust are also accepted

### The Task
We have provided you with two JSON files that contain information about Assets, both of which should contain an Asset's "Name", "Model", and "IP Address" but different naming conventions and formats:
* `Name` (Represented by 'name', 'name_snmp', 'asset-name')
* `Model` (Represented by 'model', 'asset-model')
* `IP Address` (Represented by 'ip_address', 'ipv4', 'ip-address')

In this repository you can find two sample data files:
* [`assets_1.json`](/assets_1.json).
* [`assets_2.json`](/assets_2.json).

##### Challenge Requirements
1. Create a web appication. This must be able to do the following steps
    1. Create a webpage that displays a table with the assets "Name, IP Address, Model" based on the contents in [`assets_1.json`](/assets_1.json). and [`assets_2.json`](/assets_2.json).
    2. The user should be presented an input field of free text and a submit button that will perform a matching with the assets' data fields in the above two json files based on the "Name", "Model" or "IP Address"
        The result of the submit button should display all three fields of the matched asset or "No Asset Found" in case it has failed to match anything
    
2. The system should be able to support:
    1. Larger sets of data (eg 10k+ assets)
    2. Different data formats - assets_1 and assets_2
    3. Asset 'Name', 'IP Address' and 'Model' Based matching
    4. If more than a single match is present it should match the first

3. Update the section `Installation and running this solution` in the README file explaining how to run your code

This task is aimed to evaluate your backend skills so do not worry about the UX and web application styles

### Submitting a solution
1. Clone this repository
2. Complete the problem outlined in the `Requirements` section
3. Create a new public repository under your github account with the solution (or private with with shared access with us)
4. Send us a link to your repository over email once ready

If you have any questions regarding requirements, do not hesitate to email your contact at Domotz for clarification.

### Installation and Running the solution
... TODO

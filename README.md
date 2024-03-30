# xz-backdoor-github
History of commits related to the xz backdoor Discovered On March 29, 2024: CVE-2024-3094.
Currently GitHub has taken down the repos for ToS violations. The purpose of this is to
faciliate security research of how this backdoor was snuck in over the course of 2 years of active contributions
and to search for other possible issues.
For background see: https://www.openwall.com/lists/oss-security/2024/03/29/4

## Datasets
Using ClickHouse's database of all repo events across GitHub ever, I created three datasets
of github events: the suspect users contributions, and one of all events in their shared project repo
that actually hosted the compromised releases.

### Contributions: JiaT75

Contributions by prime sispect user JiaT75 (Jia Tan). 

File:
`jiaty75_github.csv`

### Tuukani-project Repos

GitHub events (commits, comments, etc.) from https://github.com/tukaani-project
filted to before discovery (as there are a lot of unserious comments/events after discovery)

File:
`tuukani_project.csv`

### Contributions: Larhzu

Suspect user Larhzu (Lasse Collins i.e. Lars Collins, Lasse being a nickname for Lars in Scandinavia)
was also suspended by GitHub and is the only other owner on the compromised project.

File:
`larhzu_github.csv`

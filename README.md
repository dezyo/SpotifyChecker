# SpotifyChecker

Simple script to check user:pass

## Getting Started

Only download the script and install the requeriments.

### Prerequisites

Thing you need to install before running the script.

```
- Python 3.x
- Tor running with 9050 as ControlPort
- Selenim (Python library)
- Re (Python library)
```

### Example

```
for user, password in getEmailUser('txt.txt'):
	if checkAccount(user, password) == True:
		print('Valida:', user, password)
		logOut()
	else:
		print('no valida')
```

### To Do:

```
- Change time.sleep to a function to wait until the page is loaded
- Write the results into a file
```

## Authors

* **Devsc** - (https://github.com/Dezyo)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

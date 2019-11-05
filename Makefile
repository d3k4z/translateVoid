
#!/bin/sh
PREFIX = /usr

.PHONY: install
install:
	cp translateVoid.py $(DESTDIR)$(PREFIX)/bin/translateVoid
	chmod +x $(DESTDIR)$(PREFIX)/bin/translateVoid

.PHONY:clean
clean:
	sudo rm -f $(DESTDIR)$(PREFIX)/bin/translateVoid

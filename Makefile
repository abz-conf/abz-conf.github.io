#
#   Copyright (C) 2021 ABZ Conference <https://abz-conf.org>
#   All rights reserved.
#
#   Developed by: Philipp Paulweber et al.
#                 <https://github.com/abz-conf/abz-conf.github.io>
#
#   This file is part of abz-conf.github.io.
#
#   TODO
#

default: serve

.github/src/themes/academic:
	(cd .github/src/themes; ln -sf ../../lib/hugo-academic academic)

build: .github/src/themes/academic
	rm -rf .github/obj/html/*
	(cd .github/src; hugo)

serve: build
	(cd .github/src; hugo --i18n-warnings server)

serve-with-drafts: build
	(cd .github/src; hugo --i18n-warnings server -D)

clean:
	rm -rf .github/obj

# the 'deploy' target gets called by the GitHub action workflow! do not call this manually or locally
deploy: .github/src/themes/academic
	rm -rf .github/obj/html/*
	(cd .github/src; hugo --minify)
	rm -rf *.html
	cp -rf .github/obj/html/* ./

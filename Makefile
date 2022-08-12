#
#   Copyright (C) 2021-2022 ABZ Conference <https://abz-conf.org>
#   All rights reserved.
#
#   Developed by: Philipp Paulweber et al.
#                 <https://github.com/abz-conf/abz-conf.github.io/graphs/contributors>
#
#   This file is part of abz-conf.github.io.
#
#   abz-conf.github.io is licensed under a
#   Creative Commons Attribution 4.0 International License.
#
#   You should have received a copy of the license along with this
#   work. If not, see <http://creativecommons.org/licenses/by/4.0/>.
#

default: serve

build: .github/src/themes/academic
	rm -rf .github/obj/html/*
	(cd .github/src; hugo)

serve: build
	(cd .github/src; hugo server)

serve-with-drafts: build
	(cd .github/src; hugo server -D)

clean:
	rm -rf .github/obj


.github/lib/hugo-academic/.git:
	git submodule update --init

.github/src/themes/academic: .github/lib/hugo-academic/.git
	(cd .github/src/themes; ln -sf ../../lib/hugo-academic academic)


# the 'deploy' target gets called by the GitHub action workflow! do not call this manually or locally
deploy: .github/src/themes/academic
	rm -rf .github/obj/html/*
	(cd .github/src; hugo --minify)
	rm -rf *.html
	cp -rf .github/obj/html/* ./

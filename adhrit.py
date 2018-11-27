# !/usr/bin/env python

# ADHRIT is an open source tool for Android apk analysis
# and CTFs to extract maximum amount of information from an apk

import os
import argparse
from recons.apk_recon import apk_rip
from recons.apk_extract import apk_info
from recons.vapp import vapp_find
from recons.virustotal import api_check
from recons.smali_extract import smali_de
from recons.smali_extract import smali_re
from recons.smali_extract import apk_sign
from recons.smali_extract import inj_check
from recons.native_recon import native_disas
from recons.dynamic import adb_con
from recons.clean import cleaner
from recons.root import check_root

__author__ = 'Abhishek J M ( jmabhishek@gmail.com )'


class Adhrit:

    def __init__(self):
        self.apk_name = ""

    def welcome(self):
        os.system('toilet -F metal -f bigascii12 ADHRIT')
        print "| Project Page\t\t:\twww.github.com/abhi-r3v0/Adhrit"
        print "| Author\t\t:\t" + __author__
    print "\n\n"

    # Clean the tool directory for a new project
    def cleanproject(self, apk_name):
        cleaner(apk_name)

    # Extract APK information without extracting the package
    def apkripper(self, apk_name):
        apk_rip(apk_name)

    # Extract All the contents of the APK into a directory
    def apkextractor(self, apk_name):
        apk_info(apk_name)

    # Check for virtual app droppers
    def vappsearch(self, apk_name):
        vapp_find(apk_name)

    # Check if the APK has been identified by VirusTotal database
    def vtanalyzer(self, apk_name):
        api_check(apk_name)

    # Extract the source code of the APK in smali
    def smaliextractor(self, apk_name):
        smali_de(apk_name)

    # Recompile smali back into APK
    def smalirecompile(self, apk_name):
        smali_re(apk_name)

    # Sign the apk with a generic signature. For educaational purposes only!
    def apk_signing(self, apk_name):
        apk_sign(apk_name)

    # Check for string injection points
    def smali_inj(self, apk_name):
        inj_check(apk_name)

    # Identify and dump the disassembly of the native libraries within the APK
    def nativedebug(self, apk_name):
        native_disas(apk_name)

    # Install the APK in an emulator and analyze its activities
    def dynamicanalysis(apk_name):
        adb_con(apk_name)

    def checkroot(self):
        check_root()




# Main fuction starts here
def main():
    adhrit = Adhrit()
    parser = argparse.ArgumentParser(description="Help")
    parser.add_argument("-c", help="Clean up for a new project")
    parser.add_argument("-a", help="Dump package info and extract contents")
    parser.add_argument("-r", help="Analyze APK without extraction")
    parser.add_argument("-x", help="Extract APK contents only")
    parser.add_argument("-p", help="Check for virtual apps")
    parser.add_argument("-s", help="Source code of the APK in Smali")
    parser.add_argument("-b", help="Recompile smali back into APK")
    parser.add_argument("-m", help="Sign the APK")
    parser.add_argument("-i", help="Check for injection points")
    parser.add_argument("-n", help="Disassemble native libraries")
    parser.add_argument("-w", help="Welcome :P")
    parser.add_argument("-v", help="Check footprints in VirusTotal database")
    parser.add_argument("-d", help="Analyse the behaviour dynamically in a VM")
    parser.add_argument("-cr", help="Check device root status", action='store_true')
    args = parser.parse_args()

    # Adhrit Welcome ASCII
    adhrit.welcome()

    if args.c:
        adhrit.cleanproject(args.c)

    if args.a:
        adhrit.cleanproject(args.a)
        adhrit.apkripper(args.a)
        adhrit.vtanalyzer(args.a)
        adhrit.apkextractor(args.a)
        adhrit.vappsearch(args.a)
        adhrit.smaliextractor(args.a)
        adhrit.smali_inj(args.a)

    elif args.r:
        adhrit.apkripper(args.r)

    elif args.x:
        adhrit.cleanproject(args.x)
        adhrit.apkextractor(args.x)

    elif args.p:
        adhrit.vappsearch(args.p)

    elif args.s:
        adhrit.smaliextractor(args.s)

    elif args.b:
        adhrit.smalirecompile(args.b)

    elif args.m:
        adhrit.welcome()
        adhrit.apk_signing(args.m)

    elif args.i:
        adhrit.smali_inj(args.i)

    elif args.n:
        adhrit.nativedebug(args.n)

    elif args.w:
        adhrit.welcome()

    elif args.v:
        adhrit.vtanalyzer(args.v)

    elif args.d:
        adhrit.dynamicanalysis(args.d)

    elif args.cr:
        adhrit.checkroot()


if __name__ == "__main__":
    main()

# Overview

## Rules

This Macbook Pro, nicknamed *shackbook*, is public. Anyone may use it, if he or
she abides by the following rules:

 * The user shack is not and will never be a sudoer. Don't ask for it.
 * Try to minimize the customization you apply to the installed tools. It's
   okay to change them to your needs if necessary, but try not to reach a
   state where someone else is not able to use them anymore.
 * The hardware is off-limits. Do not open shackbook or remove any part of
   the hardware. This rule includes the power adaptor.
 * shackbook stays in the shack. No exceptions.
 * Do not occupy shackbook if you don't need it.
 * Do not use shackbook for evil.
 * Clean up your garbage after using shackbook. Do not leave large files.

shackbook belongs to [flyx](mailto:shack@flyx.org).

## Specs

MacBook Pro, 15 inch, Mid 2010  
2,4 GHz Intel Core i5, 8GB RAM  
Intel HD Graphics + GeForce GT 330M  
256GB SSD

shackbook suffers a curious problem where it may crash sometimes while
rendering Mission Control animations. I never experienced it crashing
somewhere else, and it doesn't happen very often (perhaps once in 8 hours). Try to avoid using Mission Control.

# Installed Software

As the user *shack* does not have administrator rights, you cannot install any
software. If you want to use some piece of software on shackbook which isn't
already installed, contact [flyx](mailto:shack@flyx.org).

All software on shackbook has been acquired legally. Do not copy commercial
software off shackbook.

## Apple Office / iLive Software

These are primarily installed for people who want to try them out.

 * Pages (word processor)
 * Numbers (spreadsheets)
 * Keynote (presentation)
 * GarageBand (music)
 * iMovie (videos)
 * Xcode (IDE)

## Text Editing

 * TextMate 2
 * Atom
 * Chocolat 2

## Interwebs

All browsers are configured to delete cookies and history when you close them.
Leave it that way. Well, all browsers except Safari, which does not have such
a setting. Please be aware of that.

 * Safari (with uBlock and JS Blocker)
 * Google Chrome (with uBlock)
 * Firefox (with uBlock and Firebug)
 * Textual (IRC client)
 * Adium (instant messaging client)

## Command Line Tools

 * iTerm (terminal emulator)
 * zsh + oh-my-zsh (shell)
 * Homebrew (package manager, kind-of)
 * ImageMagick (image conversion tools)
 * MacTeX (TeX distribution)
 * git, hg, svn, fossil
 
## Compilers and Software Development Tools

 * clang/llvm toolchain from Xcode
 * cmake
 * Java stuff: JDK 1.8, ant, maven, gradle, IntelliJ IDEA CE
 * nim
 * SourceTree (version control GUI)
 * Python stuff: python3, pip, pip3, virtualenv
 * nodejs + npm

### GCC

GCC is installed in `/opt/gnat/bin`. It is not in the PATH by default, so
that it doesn't conflict with clang/llvm. This GCC is supplied by AdaCore, it
can compile Ada, C, C++ and ObjC.

## Libraries to link against

 * boost

## Other Stuff

 * Seashore (image editing)
 * GIMP (image editing)
 * Colibricks (breakout)
 * NTFS-3g (NTFS r/w driver)
 * XLD (audio converter)
 * The Unarchiver (exactly what it says on the tin)
 * VLC (media player)
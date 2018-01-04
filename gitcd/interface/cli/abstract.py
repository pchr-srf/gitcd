import os
import simpcli

from gitcd.git.repository import Repository
from gitcd.git.branch import Branch
from gitcd.git.tag import Tag
from gitcd.git.remote import Remote

from gitcd.config import Gitcd as GitcdConfig
from gitcd.config import GitcdPersonal as GitcdPersonalConfig

from gitcd.controller import Base as BaseController

from gitcd.exceptions import GitcdNoFeatureBranchException

import sys

class BaseCommand(object):

    interface = simpcli.Interface()
    config = GitcdConfig()
    configPersonal = GitcdPersonalConfig()
    baseController = BaseController()

    def run(self, branch: Branch):
        pass

    def getDefaultBranch(self) -> Branch:
        return self.baseController.getCurrentBranch()

    def getRequestedBranch(self, branch: str) -> Branch:
        featureAsString = self.config.getString(self.config.getFeature())
        if not branch.startswith(featureAsString):
            branch = '%s%s' % (featureAsString, branch)
        return Branch(branch)

    def getRemote(self) -> str:
        remotes = self.baseController.getRemotes()

        if len(remotes) == 1:
            remote = remotes[0]
        else:
            if len(remotes) == 0:
                default = False
                choice = False
            else:
                default = remotes[0].getName()
                choice = []
                for remoteObj in remotes:
                    choice.append(remoteObj.getName())

            remoteAnswer = self.interface.askFor(
                "Which remote you want to use?",
                choice,
                default
            )
            for remoteObj in remotes:
                if remoteAnswer == remoteObj.getName():
                    remote = remoteObj

        return remote

    def checkTag(self, remote: Remote, tag: Tag) -> bool:
        repository = self.baseController.getRepository()

        if repository.hasUncommitedChanges():
            abort = self.interface.askFor(
                "You currently have uncomitted changes." +
                " Do you want me to abort and let you commit first?",
                ["yes", "no"],
                "yes"
            )

            if abort == "yes":
                sys.exit(1)

        if not remote.hasTag(branch):
            pushFeatureBranch = self.interface.askFor(
                "Your tag does not exists on remote. Do you want me to push it remote?",
                ["yes", "no"], "yes"
            )

            if pushFeatureBranch == "yes":
                remote.push(branch)

        return True

    def checkBranch(self, remote: Remote, branch: Branch) -> bool:
        repository = self.baseController.getRepository()

        # check if its a feature branch
        if not branch.isFeature():
            raise GitcdNoFeatureBranchException(
                "Your current branch is not a valid feature branch." +
                " Checkout a feature branch or pass one as param."
            )

        # check if repo has uncommited changes
        if repository.hasUncommitedChanges():
            abort = self.interface.askFor(
                "You currently have uncomitted changes." +
                " Do you want me to abort and let you commit first?",
                ["yes", "no"],
                "yes"
            )

            if abort == "yes":
                sys.exit(1)

        # check remote existence
        if not remote.hasBranch(branch):
            pushFeatureBranch = self.interface.askFor(
                "Your feature branch does not exists on remote." +
                " Do you want me to push it remote?", ["yes", "no"], "yes"
            )

            if pushFeatureBranch == "yes":
                remote.push(branch)

        # check behind origin
        if remote.isBehind(branch):

            pushFeatureBranch = self.interface.askFor(
                "Your feature branch is ahead the origin/branch." +
                " Do you want me to push the changes?",
                ["yes", "no"],
                "yes"
            )

            if pushFeatureBranch == "yes":
                remote.push(branch)

        return True

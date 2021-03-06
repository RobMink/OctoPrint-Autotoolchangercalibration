# coding=utf-8
#from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import datetime
import logging
import octoprint.plugin
import octoprint.plugin.core
import glob
import os
import sys
class AutotoolchangercalibrationPlugin( octoprint.plugin.StartupPlugin,
 octoprint.plugin.TemplatePlugin,
 octoprint.plugin.SettingsPlugin,
 octoprint.plugin.AssetPlugin,
 octoprint.plugin.SimpleApiPlugin,
 octoprint.plugin.EventHandlerPlugin):


	##~~ SettingsPlugin mixin
    def on_after_startip(self):
        self._logger.info("Hello World from AutotoolchangercalibrationPlugin")

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/AutoToolChangerCalibration.js"],
			css=["css/AutoToolChangerCalibration.css"],
			less=["less/AutoToolChangerCalibration.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
		# for details.
		return dict(
			AutoToolChangerCalibration=dict(
				displayName="Autotoolchangercalibration Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="RobMink",
				repo="OctoPrint-Autotoolchangercalibration",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/RobMink/OctoPrint-Autotoolchangercalibration/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Autotoolchangercalibration Plugin"

# Starting with OctoPrint 1.4.0 OctoPrint will also support to run under Python 3 in addition to the deprecated
# Python 2. New plugins should make sure to run under both versions for now. Uncomment one of the following
# compatibility flags according to what Python versions your plugin supports!
__plugin_pythoncompat__ = ">=3,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AutotoolchangercalibrationPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
